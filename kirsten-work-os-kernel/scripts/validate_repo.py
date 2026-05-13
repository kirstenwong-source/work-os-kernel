#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kirsten_work_os_kernel.validators import validate_repo


def main() -> int:
    failures = validate_repo(ROOT)
    if failures:
        print(json.dumps({"status": "failed", "failures": failures}, indent=2))
        return 1
    print(json.dumps({"status": "ok", "failures": []}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
