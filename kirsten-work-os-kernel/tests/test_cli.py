from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPPORTUNITY = ROOT / "examples" / "phd-outreach" / "google_phd_outreach_opportunity.json"
PROFILE = ROOT / "data" / "canonical" / "profile" / "kirsten_profile.json"
SIGNAL = ROOT / "examples" / "phd-outreach" / "google_phd_outreach_signal.json"


def run_cli(*args: str):
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    return subprocess.run(
        [sys.executable, "-m", "kirsten_work_os_kernel", *args],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_cli_validate():
    result = run_cli("validate", "--root", str(ROOT))
    assert result.returncode == 0, result.stderr + result.stdout
    assert json.loads(result.stdout)["status"] == "ok"


def test_cli_build_outputs(tmp_path):
    branch_out = tmp_path / "branch.json"
    brief_out = tmp_path / "brief.md"
    signal_out = tmp_path / "signal.json"

    result = run_cli("build-branch", "--opportunity", str(OPPORTUNITY), "--profile", str(PROFILE), "--out", str(branch_out))
    assert result.returncode == 0, result.stderr + result.stdout
    assert branch_out.exists()

    result = run_cli("build-brief", "--opportunity", str(OPPORTUNITY), "--profile", str(PROFILE), "--out", str(brief_out))
    assert result.returncode == 0, result.stderr + result.stdout
    assert "Strategy Brief" in brief_out.read_text(encoding="utf-8")

    result = run_cli("intake-signal", "--signal", str(SIGNAL), "--out", str(signal_out))
    assert result.returncode == 0, result.stderr + result.stdout
    assert json.loads(signal_out.read_text(encoding="utf-8"))["status"] == "captured_for_review"
