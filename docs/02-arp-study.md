# Experiment 2 — Address Resolution Protocol (ARP)

## Aim
Observe how an IPv4 host discovers the link-layer address associated with a local neighbour.

## Procedure
1. Find the default gateway using `ip route`.
2. Inspect cached entries using `ip neigh`.
3. Start a capture: `sudo bash scripts/capture_traffic.sh <interface> arp 20`.
4. While capturing, generate local-subnet traffic (for example, ping your gateway).
5. Open the capture in Wireshark and apply `arp`.

## Fields to inspect
- Operation: request or reply
- Sender MAC and sender IPv4 address
- Target MAC and target IPv4 address
- Whether the request is broadcast

## Observation sheet
| Packet | Operation | Sender IPv4 | Sender MAC | Target IPv4 | Target MAC |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

## Questions
- Why is an ARP request commonly broadcast on a LAN?
- Why can an ARP reply be unicast?
- What is the purpose of the neighbour cache?

## Conclusion
Summarise the request/reply exchange visible in your own capture.
