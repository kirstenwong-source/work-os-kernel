from __future__ import annotations

from pathlib import Path

from kirsten_work_os_kernel.validators import validate_repo

ROOT = Path(__file__).resolve().parents[1]


def test_repo_validation_is_green():
    assert validate_repo(ROOT) == []
