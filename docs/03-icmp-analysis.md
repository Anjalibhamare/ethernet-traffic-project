# Experiment 3 — ICMP Traffic Analysis

## Aim
Generate ICMP Echo Request and Echo Reply packets and analyse their IP and ICMP fields.

## Theory
ICMP supports diagnostic and error-reporting functions in IP networks. `ping` commonly uses Echo Request and Echo Reply messages to test reachability and estimate round-trip time. Firewalls may filter ICMP, so a missing reply does not necessarily mean that a host is offline.

## Procedure
1. Select a reachable lab host or local gateway; test only permitted destinations.
2. Identify the outgoing interface using `ip route get <destination-ip>`.
3. Start capture: `sudo bash scripts/capture_traffic.sh <interface> icmp 25`.
4. During capture run: `ping -c 4 <destination-ip>`.
5. Open the capture in Wireshark and apply `icmp`.
6. Select a request and reply; expand IPv4 and ICMP details.

## Fields to record
Source/destination IP; ICMP type/code; identifier; sequence number; IPv4 TTL; packet length; ping RTT and packet loss.

## Observation table
| Packet | Source IP | Destination IP | Type/code | Identifier | Sequence | TTL |
|---|---|---|---|---|---|---|
| Echo request 1 | | | | | | |
| Echo reply 1 | | | | | | |
| Echo request 2 | | | | | | |
| Echo reply 2 | | | | | | |

## Ping statistics
| Metric | Measured value |
|---|---|
| Transmitted | |
| Received | |
| Packet loss | |
| Min/average/max RTT | |

## Screenshot
Add Wireshark evidence as `screenshots/03_icmp_echo_packets.png`.

## Conclusion
Describe the request/reply pattern and ping statistics. Note filtering or packet loss if present.

## Viva
1. What is ICMP used for?
2. What are Echo Request and Echo Reply?
3. Which utility generates ICMP Echo messages?
4. What does TTL represent?
5. Does no Echo Reply prove that a host is down?
