#!/usr/bin/env python3
"""Collect local Linux interface, address, route and neighbour information."""
from __future__ import annotations
import argparse
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

COMMANDS = [
    ("Link status", ["ip", "-brief", "link"]),
    ("IP addresses", ["ip", "-brief", "address"]),
    ("Routing table", ["ip", "route"]),
    ("Neighbour table", ["ip", "neigh"]),
]

def run_command(command: list[str]) -> tuple[int, str]:
    if not shutil.which(command[0]):
        return 127, f"Required command not found: {command[0]}"
    try:
        result = subprocess.run(command, check=False, capture_output=True, text=True, timeout=15)
        output = result.stdout.strip()
        if result.stderr.strip():
            output += ("\n" if output else "") + f"[stderr] {result.stderr.strip()}"
        return result.returncode, output or "(command returned no output)"
    except subprocess.TimeoutExpired:
        return 124, f"Timed out: {' '.join(command)}"
    except OSError as exc:
        return 1, f"Could not run command: {exc}"

def build_report() -> str:
    lines = ["# Network configuration snapshot", f"Collected at (UTC): {datetime.now(timezone.utc).isoformat()}", f"Platform: {platform.platform()}", f"Python: {platform.python_version()}"]
    for title, command in COMMANDS:
        status, output = run_command(command)
        lines.extend(["", f"## {title}", f"Command: {' '.join(command)}", f"Exit status: {status}", "```text", output, "```"])
    return "\n".join(lines) + "\n"

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path to save the report")
    args = parser.parse_args()
    report = build_report()
    print(report, end="")
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(report, encoding="utf-8")
            print(f"\nSaved report to {args.output}", file=sys.stderr)
        except OSError as exc:
            print(f"Could not save report: {exc}", file=sys.stderr)
            return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
