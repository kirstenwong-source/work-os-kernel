from __future__ import annotations

from pathlib import Path
from typing import Any

from .ids import new_id, utc_now
from .io import read_json


def _lower_set(values: list[str]) -> set[str]:
    return {v.lower().strip() for v in values}


def build_branch_packet(opportunity_path: str | Path, profile_path: str | Path) -> dict[str, Any]:
    opportunity = read_json(opportunity_path)
    profile = read_json(profile_path)

    strengths = _lower_set(profile.get("strengths", []))
    required = opportunity.get("required_capabilities", [])
    preferred = opportunity.get("preferred_capabilities", [])

    matched_required = [cap for cap in required if any(token in " ".join(strengths) for token in cap.lower().split())]
    matched_preferred = [cap for cap in preferred if any(token in " ".join(strengths) for token in cap.lower().split())]

    return {
        "schema_id": "branch_packet.v1",
        "packet_id": new_id("branch_packet"),
        "created_at": utc_now(),
        "branch_id": opportunity["branch_id"],
        "opportunity_id": opportunity["opportunity_id"],
        "opportunity_title": opportunity["title"],
        "organization": opportunity["organization"],
        "candidate_positioning": profile["positioning"],
        "strategic_thesis": opportunity["strategic_thesis"],
        "matched_required_capabilities": matched_required,
        "matched_preferred_capabilities": matched_preferred,
        "evidence_refs": sorted(set(profile.get("evidence_refs", []) + opportunity.get("evidence_refs", []))),
        "portfolio_projects": opportunity.get("portfolio_projects", []),
        "recommended_next_actions": [
            "Lead with university ecosystem strategy, not generic student affairs administration.",
            "Translate program leadership into talent outreach operations.",
            "Make data-informed decision-making visible through the dashboard project.",
            "Use research translation language to address the technical-outlook requirement.",
            "Build relationship artifacts that show faculty, lab, and internal stakeholder fluency."
        ]
    }


def branch_packet_to_markdown(packet: dict[str, Any]) -> str:
    projects = "\n".join(f"- {item}" for item in packet.get("portfolio_projects", [])) or "- None listed"
    evidence = "\n".join(f"- {item}" for item in packet.get("evidence_refs", [])) or "- None listed"
    actions = "\n".join(f"- {item}" for item in packet.get("recommended_next_actions", [])) or "- None listed"
    return f"""# Branch Packet: {packet['opportunity_title']}

Organization: {packet['organization']}  
Branch: `{packet['branch_id']}`  
Packet: `{packet['packet_id']}`  
Created: {packet['created_at']}

## Candidate positioning

{packet['candidate_positioning']}

## Strategic thesis

{packet['strategic_thesis']}

## Evidence references

{evidence}

## Portfolio projects

{projects}

## Recommended next actions

{actions}
"""
