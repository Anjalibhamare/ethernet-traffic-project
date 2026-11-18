#!/usr/bin/env bash
# Capture a short, filtered lab trace. Requires tcpdump and permission to capture.
set -euo pipefail
IFACE="${1:-lo}"
PROTO="${2:-udp}"
DURATION="${3:-20}"
OUTDIR="captures"
mkdir -p "$OUTDIR"
case "$PROTO" in
  arp) FILTER="arp" ;;
  icmp) FILTER="icmp" ;;
  tcp) FILTER="tcp" ;;
  udp) FILTER="udp" ;;
  all) FILTER="" ;;
  *) echo "Usage: sudo $0 <interface> <arp|icmp|tcp|udp|all> [seconds]" >&2; exit 2 ;;
esac
if ! command -v tcpdump >/dev/null 2>&1; then
  echo "tcpdump is required. Install it with your distribution package manager." >&2
  exit 1
fi
STAMP="$(date +%Y%m%d_%H%M%S)"
FILE="$OUTDIR/${PROTO}_${STAMP}.pcap"
echo "Capturing on $IFACE for $DURATION seconds -> $FILE"
if [[ -n "$FILTER" ]]; then
  timeout "$DURATION" tcpdump -i "$IFACE" -nn -s 0 -w "$FILE" "$FILTER" || STATUS=$?
else
  timeout "$DURATION" tcpdump -i "$IFACE" -nn -s 0 -w "$FILE" || STATUS=$?
fi
if [[ "${STATUS:-0}" -gt 1 ]]; then
  echo "Capture ended with status ${STATUS}; inspect the message above." >&2
  exit "$STATUS"
fi
echo "Saved capture: $FILE"
echo "Open it with: wireshark '$FILE'"
