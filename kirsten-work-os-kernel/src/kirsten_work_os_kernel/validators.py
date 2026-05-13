from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REQUIRED_PATHS = [
    "README.md",
    "AI_WORK_START_HERE.md",
    "DATA_FLOW_MAP.md",
    "ENDPOINTS_AND_COMMANDS.md",
    "governance/PROMOTION_POLICY.md",
    "registry/source-of-truth.json",
    "registry/schema-registry.json",
    "registry/branch-registry.json",
    "data/canonical/profile/kirsten_profile.json",
    "branches/phd-outreach/branch.json",
    "examples/phd-outreach/google_phd_outreach_opportunity.json",
]

JSON_OBJECT_DIRS = [
    "data/canonical",
    "data/evidence",
    "branches",
    "examples",
]


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_map(root: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    failures: list[str] = []
    registry_path = root / "registry" / "schema-registry.json"
    try:
        registry = _load_json(registry_path)
    except Exception as exc:
        return {}, [f"Cannot read schema registry: {exc}"]

    schemas: dict[str, dict[str, Any]] = {}
    for entry in registry.get("schemas", []):
        schema_id = entry.get("id")
        rel_path = entry.get("path")
        if not schema_id or not rel_path:
            failures.append("Schema registry entry missing id or path")
            continue
        schema_path = root / rel_path
        if not schema_path.exists():
            failures.append(f"Schema path missing: {rel_path}")
            continue
        try:
            schemas[schema_id] = _load_json(schema_path)
        except Exception as exc:
            failures.append(f"Schema path does not parse as JSON: {rel_path}: {exc}")
    return schemas, failures


def _validate_basic_schema(obj: dict[str, Any], schema: dict[str, Any], rel_path: str) -> list[str]:
    failures: list[str] = []
    for field in schema.get("required", []):
        if field not in obj:
            failures.append(f"{rel_path} missing required field {field}")
    properties = schema.get("properties", {})
    for field, spec in properties.items():
        if field not in obj:
            continue
        expected = spec.get("type")
        value = obj[field]
        if expected == "string" and not isinstance(value, str):
            failures.append(f"{rel_path} field {field} should be string")
        elif expected == "array" and not isinstance(value, list):
            failures.append(f"{rel_path} field {field} should be array")
        elif expected == "object" and not isinstance(value, dict):
            failures.append(f"{rel_path} field {field} should be object")
    return failures


def validate_repo(root: str | Path) -> list[str]:
    root_path = Path(root).resolve()
    failures: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (root_path / rel).exists():
            failures.append(f"Required path missing: {rel}")

    schemas, schema_failures = _schema_map(root_path)
    failures.extend(schema_failures)

    try:
        source_truth = _load_json(root_path / "registry" / "source-of-truth.json")
        for entry in source_truth.get("authority_order", []):
            rel = entry.get("path")
            if rel and not (root_path / rel).exists():
                failures.append(f"Source-of-truth path missing: {rel}")
    except Exception as exc:
        failures.append(f"Cannot validate source-of-truth registry: {exc}")

    try:
        branch_registry = _load_json(root_path / "registry" / "branch-registry.json")
        for branch in branch_registry.get("branches", []):
            rel = branch.get("path")
            if not rel or not (root_path / rel).exists():
                failures.append(f"Branch registry target missing: {rel}")
    except Exception as exc:
        failures.append(f"Cannot validate branch registry: {exc}")

    for rel_dir in JSON_OBJECT_DIRS:
        base = root_path / rel_dir
        if not base.exists():
            failures.append(f"JSON object directory missing: {rel_dir}")
            continue
        for path in sorted(base.rglob("*.json")):
            rel_path = path.relative_to(root_path).as_posix()
            try:
                obj = _load_json(path)
            except Exception as exc:
                failures.append(f"JSON object cannot parse: {rel_path}: {exc}")
                continue
            if not isinstance(obj, dict):
                failures.append(f"JSON object should be an object: {rel_path}")
                continue
            schema_id = obj.get("schema_id")
            if schema_id in schemas:
                failures.extend(_validate_basic_schema(obj, schemas[schema_id], rel_path))

    return failures
