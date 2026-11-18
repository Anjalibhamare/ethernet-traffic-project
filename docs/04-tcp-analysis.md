# Experiment 4 — TCP Traffic Analysis

## Aim
Capture a TCP flow and study connection establishment, ports, flags, sequence numbers, acknowledgements and data transfer.

## Theory
TCP is connection-oriented and provides reliable, ordered byte-stream delivery. A typical connection begins with a three-way handshake: SYN, SYN-ACK and ACK. TCP headers include ports, sequence and acknowledgement numbers, flags, window information and other fields. Actual ports and packet sequences depend on the application and network.

## Procedure
1. Determine the interface used for the destination with `ip route get 1.1.1.1`.
2. Start a capture: `sudo bash scripts/capture_traffic.sh <interface> tcp 30`.
3. During capture run `curl -I --max-time 10 https://example.com` (or an approved test server).
4. Open the capture in Wireshark and apply `tcp`.
5. Identify a connection and locate SYN, SYN-ACK and ACK when visible.
6. Inspect data packets and optionally select Follow → TCP Stream.

## Fields
Source/destination IP and TCP ports; flags; sequence and acknowledgement numbers; TCP header length; window size; payload length.

## Observation table
| Segment | Source:port | Destination:port | Flags | Seq/Ack | Payload length |
|---|---|---|---|---|---|
| SYN | | | | | |
| SYN-ACK | | | | | |
| ACK | | | | | |
| Data | | | | | |

## Analysis
Explain how the handshake establishes sequence-number state, and how acknowledgements and retransmission support reliable delivery. A capture may not contain a complete handshake; record only what is present.

## Screenshot
Add Wireshark evidence as `screenshots/04_tcp_handshake.png`.

## Conclusion
Describe the TCP connection and identify flags and ports measured in your capture.

## Viva
1. Why is TCP connection-oriented?
2. Explain the three-way handshake.
3. Purpose of sequence and acknowledgement numbers?
4. Difference between SYN and ACK?
5. What is retransmission?
6. What are TCP port numbers?
