# AI Table Of Contents

## Orientation

- `README.md` - project overview and quick start
- `AI_WORK_START_HERE.md` - AI and collaborator operating rules
- `DATA_FLOW_MAP.md` - how objects move through the kernel
- `ENDPOINTS_AND_COMMANDS.md` - available local commands
- `FOLDER_SEMANTICS.md` - what belongs where
- `RECENT_WORK.md` - current status and last changes

## Control plane

- `governance/` - policies and promotion rules
- `registry/` - source-of-truth, schema, branch, and command registries
- `schemas/` - JSON schemas for governed objects
- `data/canonical/` - stable career evidence and profile objects

## Evidence plane

- `data/evidence/` - grounded evidence objects and source references
- `data/runtime/` - local generated outputs; safe to regenerate

## Execution plane

- `src/kirsten_work_os_kernel/` - local Python package
- `scripts/` - command wrappers
- `tests/` - green-check suite
- `.github/workflows/ci.yml` - GitHub Actions validation

## Branches

- `branches/_template/` - template for new workstreams
- `branches/phd-outreach/` - first active branch
- `examples/phd-outreach/` - sample opportunity and signal objects
