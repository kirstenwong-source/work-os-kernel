from __future__ import annotations

from pathlib import Path

from .io import read_json


def build_brief(opportunity_path: str | Path, profile_path: str | Path) -> str:
    opportunity = read_json(opportunity_path)
    profile = read_json(profile_path)

    required = "\n".join(f"- {cap}" for cap in opportunity.get("required_capabilities", []))
    preferred = "\n".join(f"- {cap}" for cap in opportunity.get("preferred_capabilities", []))
    strengths = "\n".join(f"- {cap}" for cap in profile.get("strengths", []))
    projects = "\n".join(f"- {proj}" for proj in opportunity.get("portfolio_projects", []))

    return f"""# Strategy Brief: {opportunity['title']} at {opportunity['organization']}

## Core positioning

{profile['positioning']}

## Opportunity thesis

{opportunity['strategic_thesis']}

## What the role appears to need

### Required capabilities

{required}

### Preferred capabilities

{preferred}

## Kirsten's reusable strengths

{strengths}

## Portfolio projects that should support this branch

{projects}

## Message to reinforce

Kirsten should be framed as a university ecosystem strategist who can build high-trust academic relationships, design data-informed outreach programs, and translate complex research or institutional contexts into practical engagement strategy.

## Risk to manage

The main risk is that reviewers may read a student affairs and residence life background too narrowly. The application materials should translate the background into academic partnership, talent outreach, stakeholder engagement, program operations, and research translation language.
"""
