# Capture a short protocol-filtered trace. Use only on networks you are authorised to inspect.
set -Eeuo pipefail
usage(){ echo 'Usage: sudo bash scripts/capture_traffic.sh <interface> <arp|icmp|tcp|udp|all> [seconds]'; }
IFACE="${1:-}"; PROTO="${2:-}"; DURATION="${3:-20}"
if [[ -z "$IFACE" || -z "$PROTO" ]]; then usage >&2; exit 2; fi
if ! [[ "$DURATION" =~ ^[1-9][0-9]*$ ]]; then echo 'Duration must be a positive integer.' >&2; exit 2; fi
case "$PROTO" in arp) FILTER=arp;; icmp) FILTER=icmp;; tcp) FILTER=tcp;; udp) FILTER=udp;; all) FILTER='';; *) usage >&2; exit 2;; esac
command -v tcpdump >/dev/null || { echo 'tcpdump is not installed.' >&2; exit 1; }
mkdir -p captures
STAMP="$(date +%Y%m%d_%H%M%S)"; OUT="captures/${PROTO}_${STAMP}.pcap"
echo "Capturing $PROTO on $IFACE for $DURATION seconds -> $OUT"
ARGS=(-i "$IFACE" -nn -s 0 -U -w "$OUT"); [[ -z "$FILTER" ]] || ARGS+=("$FILTER")
set +e; timeout --signal=INT "$DURATION" tcpdump "${ARGS[@]}"; STATUS=$?; set -e
if [[ $STATUS -ne 0 && $STATUS -ne 124 && $STATUS -ne 130 ]]; then echo "Capture failed with status $STATUS" >&2; exit "$STATUS"; fi
if [[ -s "$OUT" ]]; then echo "Saved: $OUT"; echo "Open: wireshark '$OUT'"; else echo 'No packets saved; check interface and generate matching traffic.' >&2; exit 1; fi
