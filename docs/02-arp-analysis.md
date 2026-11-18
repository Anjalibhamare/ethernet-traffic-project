# Experiment 2 — ARP Protocol Analysis

## Aim
Observe ARP requests and replies and understand how a local IPv4 address is associated with a MAC address.

## Theory
ARP discovers the link-layer address associated with an IPv4 neighbour on a local network. A host without a usable mapping may broadcast an ARP request. The device owning the queried address can respond with an ARP reply, and the mapping may be cached. IPv6 uses Neighbor Discovery Protocol, not ARP.

## Procedure
1. Identify the active interface with `ip -brief link`.
2. Identify the gateway using `ip route`; alternatively use an authorised host on the same subnet.
3. Inspect mappings with `ip neigh`.
4. Start capture: `sudo bash scripts/capture_traffic.sh <interface> arp 25`.
5. While capture is active, ping the local gateway or lab host: `ping -c 2 <gateway-ip>`.
6. Open the capture in Wireshark and apply `arp`.
7. Expand the ARP details and inspect the request and reply.

## Fields
Opcode; sender MAC/IP; target MAC/IP; hardware type; protocol type; destination Ethernet address.

## Observation table
| Frame | Opcode | Sender IPv4 | Sender MAC | Target IPv4 | Target MAC |
|---|---|---|---|---|---|
| Request | | | | | |
| Reply | | | | | |

## Analysis
Explain why a request is normally broadcast on the LAN and how the reply supplies the MAC mapping. Compare the packet fields with `ip neigh` output.

## Screenshot
Add Wireshark evidence as `screenshots/02_arp_request_reply.png`.

## Conclusion
Summarise the exchange from your own capture; IP and MAC values vary by environment.

## Viva
1. What is ARP?
2. Why is an ARP request broadcast?
3. Difference between request and reply?
4. What is the neighbour cache?
5. Does IPv6 use ARP?
