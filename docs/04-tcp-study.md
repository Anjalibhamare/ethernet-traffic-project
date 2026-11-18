# Experiment 4 — TCP connection analysis

## Aim
Identify TCP connection establishment and inspect TCP header fields.

## Procedure
1. Start a short capture on the interface used by your test application: `sudo bash scripts/capture_traffic.sh <interface> tcp 30`.
2. In another terminal, generate a permitted test connection, e.g. `curl -I https://example.com`.
3. Open the capture in Wireshark and apply `tcp`.
4. Select one connection and use **Follow → TCP Stream** if useful.
5. Identify SYN, SYN-ACK and ACK where the complete handshake is present.

## Observation sheet
| Segment | Source:port | Destination:port | Flags | Seq/Ack | Payload length |
|---|---|---|---|---|---|
| SYN | | | | | |
| SYN-ACK | | | | | |
| ACK | | | | | |
| Data | | | | | |

## Analysis
Explain the three-way handshake and how sequence/acknowledgment numbers support reliable ordered delivery. Port numbers and packet sizes depend on the application and capture.

## Questions
- Why does TCP use a handshake?
- What is the difference between SYN and ACK?
- What is retransmission?

## Conclusion
Describe the TCP flow you observed; do not assume every capture contains a complete handshake.
