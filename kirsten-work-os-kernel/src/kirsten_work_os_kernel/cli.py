from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .branch_builder import build_branch_packet, branch_packet_to_markdown
from .brief_builder import build_brief
from .io import write_json, write_text
from .signal_intake import intake_signal
from .validators import validate_repo


def _cmd_validate(args: argparse.Namespace) -> int:
    failures = validate_repo(args.root)
    if failures:
        print(json.dumps({"status": "failed", "failures": failures}, indent=2))
        return 1
    print(json.dumps({"status": "ok", "failures": []}, indent=2))
    return 0


def _cmd_build_branch(args: argparse.Namespace) -> int:
    packet = build_branch_packet(args.opportunity, args.profile)
    out = Path(args.out)
    if out.suffix.lower() == ".md":
        write_text(out, branch_packet_to_markdown(packet))
    else:
        write_json(out, packet)
    print(json.dumps({"status": "ok", "out": str(out)}, indent=2))
    return 0


def _cmd_build_brief(args: argparse.Namespace) -> int:
    brief = build_brief(args.opportunity, args.profile)
    write_text(args.out, brief)
    print(json.dumps({"status": "ok", "out": str(args.out)}, indent=2))
    return 0


def _cmd_intake_signal(args: argparse.Namespace) -> int:
    record = intake_signal(args.signal)
    write_json(args.out, record)
    print(json.dumps({"status": "ok", "out": str(args.out)}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kirsten-work-os")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate repo structure and registered objects")
    validate.add_argument("--root", default=".")
    validate.set_defaults(func=_cmd_validate)

    branch = sub.add_parser("build-branch", help="Build a branch packet")
    branch.add_argument("--opportunity", required=True)
    branch.add_argument("--profile", required=True)
    branch.add_argument("--out", required=True)
    branch.set_defaults(func=_cmd_build_branch)

    brief = sub.add_parser("build-brief", help="Build a strategy brief")
    brief.add_argument("--opportunity", required=True)
    brief.add_argument("--profile", required=True)
    brief.add_argument("--out", required=True)
    brief.set_defaults(func=_cmd_build_brief)

    signal = sub.add_parser("intake-signal", help="Capture a work signal as a runtime record")
    signal.add_argument("--signal", required=True)
    signal.add_argument("--out", required=True)
    signal.set_defaults(func=_cmd_intake_signal)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
