#!/usr/bin/env python3
"""Collect a read-only snapshot of local Linux network configuration."""
import platform
import shutil
import subprocess
from datetime import datetime, timezone

COMMANDS = {
    "Interfaces and addresses": ["ip", "-brief", "address"],
    "Routing table": ["ip", "route"],
    "Neighbour table": ["ip", "neigh"],
}

def main():
    print("Ethernet Traffic Lab - Network Snapshot")
    print("Timestamp (UTC):", datetime.now(timezone.utc).isoformat())
    print("Platform:", platform.platform())
    for title, command in COMMANDS.items():
        print(f"\n## {title}")
        if not shutil.which(command[0]):
            print(f"Skipped: {command[0]} is not installed.")
            continue
        result = subprocess.run(command, text=True, capture_output=True, check=False)
        print(result.stdout.rstrip() or result.stderr.rstrip() or "(no output)")
        if result.returncode:
            print("Command exit status:", result.returncode)

if __name__ == "__main__":
    main()
