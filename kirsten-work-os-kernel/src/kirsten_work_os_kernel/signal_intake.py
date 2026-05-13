from __future__ import annotations

from pathlib import Path
from typing import Any

from .ids import new_id, utc_now
from .io import read_json


def intake_signal(signal_path: str | Path) -> dict[str, Any]:
    signal = read_json(signal_path)
    return {
        "schema_id": "signal_record.v1",
        "record_id": new_id("signal_record"),
        "created_at": utc_now(),
        "source_signal_id": signal["signal_id"],
        "branch_id": signal["branch_id"],
        "signal_type": signal["signal_type"],
        "summary": signal["summary"],
        "source_ref": signal["source_ref"],
        "recommended_action": signal["recommended_action"],
        "status": "captured_for_review",
        "next_steps": [
            "Confirm source evidence.",
            "Connect signal to a branch contract.",
            "Decide which artifact should be generated next.",
            "Promote only reviewed facts into canonical data."
        ]
    }
