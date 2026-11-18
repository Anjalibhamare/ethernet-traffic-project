# Ethernet Communication Investigation and Traffic Analysis — Lab Report

> Complete this after running the experiments. Replace prompts with your own observations and insert your screenshots.

## Project details
- Student name: [Name]
- Roll number: [Roll number]
- Class/course: [Class/course]
- Operating system: [Linux distribution/version]
- Experiment dates: [Dates]

## Abstract
[Summarise the aim, tools, protocols investigated and your measured findings.]

## Problem statement
Network protocol activity is not directly visible to an application user. This practical study uses controlled traffic generation and packet analysis to make network addressing and transport protocol behaviour observable.

## Objectives
[Summarise the objectives from the README.]

## Requirements
[Record your system, Linux distribution, Python version, Wireshark/tshark, tcpdump and utilities.]

## Experiment 1 — Network baseline
- Commands: [Commands used]
- Interface/address observations: [Measured values]
- Screenshot: [01_network_interfaces.png]
- Result/conclusion: [Your conclusion]

## Experiment 2 — ARP
- Interface: [Interface]
- Request fields: [Measured values]
- Reply fields: [Measured values]
- Screenshot: [02_arp_request_reply.png]
- Result/conclusion: [Your conclusion]

## Experiment 3 — ICMP
- Destination: [Destination]
- Ping statistics: [Measured values]
- ICMP fields: [Measured values]
- Screenshot: [03_icmp_echo_packets.png]
- Result/conclusion: [Your conclusion]

## Experiment 4 — TCP
- Test application/destination: [Details]
- Ports and flags: [Measured values]
- Handshake observed: [Yes/no/partial, explain]
- Screenshot: [04_tcp_handshake.png]
- Result/conclusion: [Your conclusion]

## Experiment 5 — UDP
- Client/server endpoint: [Measured values]
- Packet length and payload: [Measured values]
- Screenshot: [05_udp_client_server.png]
- Result/conclusion: [Your conclusion]

## Overall conclusion
[Summarise what you learned. Distinguish measured results from theoretical expectations.]

## References
- Linux manual pages: `ip(8)`, `ping(8)`, `tcpdump(8)`
- Wireshark User's Guide: https://www.wireshark.org/docs/
- Python socket documentation: https://docs.python.org/3/library/socket.html
- RFC 826 — An Ethernet Address Resolution Protocol
- RFC 792 — Internet Control Message Protocol
- RFC 9293 — Transmission Control Protocol
- RFC 768 — User Datagram Protocol
