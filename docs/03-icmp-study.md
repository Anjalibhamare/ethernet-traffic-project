# Experiment 3 — ICMP traffic analysis

## Aim
Generate and inspect ICMP Echo Requests and Echo Replies.

## Procedure
1. Select a permitted, reachable destination (prefer a lab host or your gateway).
2. Start a capture: `sudo bash scripts/capture_traffic.sh <interface> icmp 20`.
3. During capture run `ping -c 4 <destination-ip>`.
4. Open the resulting capture and apply the `icmp` display filter.

## Fields to record
| Packet | Source IP | Destination IP | ICMP type/code | Identifier | Sequence | TTL |
|---|---|---|---|---|---|---|
| Request 1 | | | | | | |
| Reply 1 | | | | | | |

## Analysis
Compare request and reply types, sequence values and round-trip times from ping. A missing reply may be caused by filtering or policy and does not alone prove that a host is offline.

## Questions
- What is the purpose of ICMP?
- What do Echo Request and Echo Reply mean?
- What does TTL limit?

## Conclusion
Use the packets and ping output you actually collected.
