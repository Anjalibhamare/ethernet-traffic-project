#!/usr/bin/env python3
"""Summarise packet counts and protocol hierarchy from a capture using tshark."""
import argparse, shutil, subprocess, sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('capture',type=Path)
    args=parser.parse_args()
    if not args.capture.is_file(): parser.error(f'capture file does not exist: {args.capture}')
    tshark=shutil.which('tshark')
    if not tshark:
        print('tshark is not installed. Install Wireshark/tshark first.',file=sys.stderr); return 2
    for label,extra in [('Capture statistics',['-z','io,stat,0']),('Protocol hierarchy',['-z','io,phs'])]:
        print(f'\n## {label}')
        result=subprocess.run([tshark,'-r',str(args.capture),'-q',*extra],capture_output=True,text=True,check=False)
        print(result.stdout.strip() or result.stderr.strip() or '(no summary output)')
        if result.returncode: return result.returncode
    return 0
if __name__=='__main__': raise SystemExit(main())
