# Experiment 5 — UDP Traffic Analysis

## Aim
Generate UDP datagrams between a local Python client and server and inspect their fields using Wireshark.

## Theory
UDP is connectionless. It carries datagrams with source and destination ports, length, checksum and payload. UDP does not provide TCP-style connection establishment, retransmission or ordered delivery guarantees. An application may implement its own response mechanism; that does not change UDP's transport properties.

## Procedure
1. Terminal 1: `python3 scripts/udp_server.py`.
2. Terminal 2: `sudo bash scripts/capture_traffic.sh lo udp 25`.
3. During capture, terminal 3: `python3 scripts/udp_client.py --message "My UDP experiment"`.
4. Observe the client response and server log.
5. Open the capture in Wireshark and apply `udp.port == 5005`.
6. Inspect the outgoing datagram and server response.

## Fields
Source/destination IP and UDP ports; UDP length; checksum; payload; datagram count in each direction.

## Observation table
| Parameter | Client datagram | Server response |
|---|---|---|
| Source IP | | |
| Destination IP | | |
| Source port | | |
| Destination port | | |
| UDP length | | |
| Payload | | |

## Analysis
Explain why the client datagram is sent without a TCP-style handshake. The example server's ACK is an application response, not a reliability feature built into UDP.

## Screenshot
Add evidence as `screenshots/05_udp_client_server.png`.

## Conclusion
Summarise your own UDP request/response and include measured ports and packet lengths.

## Viva
1. What is UDP?
2. Why is it connectionless?
3. Which fields appear in a UDP header?
4. Does UDP guarantee delivery or ordering?
5. Give applications that may use UDP.
6. Is the server response a built-in UDP acknowledgement?
