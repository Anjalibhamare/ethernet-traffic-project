# Ethernet Communication Investigation and Traffic Analysis Using Linux

## Project overview
This project investigates Ethernet networking and related TCP/IP protocols through Linux diagnostics, controlled traffic generation, packet capture, and Wireshark analysis.

## Problem statement
Network communication is often treated as a black box. Although applications exchange data continuously, addressing information, protocol headers, connection setup, and packet flow are not always visible to learners. This project provides a structured workflow to generate controlled network traffic, capture packets, interpret protocol fields, and relate observations to Ethernet and TCP/IP operation.

## Objectives
- Inspect network interfaces, MAC addresses, IPv4 addresses, and routing information.
- Understand ARP neighbour discovery and IPv4-to-MAC mapping.
- Generate ICMP Echo traffic and inspect request/reply packets.
- Observe TCP connection establishment, ports, flags, and data segments.
- Generate UDP traffic with a local Python client/server.
- Capture and analyse traffic using Wireshark and command-line tools.

## Requirements
Linux (Ubuntu, Debian, Pop!_OS or equivalent), Python 3.9+, Wireshark/tshark, tcpdump, iproute2, ping and curl. Packet capture may require sudo.

Install on Ubuntu/Debian:
```bash
sudo apt update
sudo apt install -y python3 python3-venv wireshark tshark tcpdump iproute2 iputils-ping curl
```

## Repository structure
```text
.
├── README.md
├── requirements.txt
├── docs/
│   ├── 01-network-baseline.md
│   ├── 02-arp-analysis.md
│   ├── 03-icmp-analysis.md
│   ├── 04-tcp-analysis.md
│   ├── 05-udp-analysis.md
│   └── report-template.md
├── scripts/
│   ├── network_snapshot.py
│   ├── protocol_summary.py
│   ├── capture_traffic.sh
│   ├── udp_server.py
│   └── udp_client.py
├── results/
├── captures/
└── screenshots/
```

## Setup
```bash
git clone https://github.com/Anjalibhamare/ethernet-traffic-project.git
cd ethernet-traffic-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Core scripts use Python's standard library; Scapy is optional.

## Experiments
| No. | Experiment | Tools | Learning outcome |
|---|---|---|---|
| 1 | Network interface and addressing baseline | ip, Python snapshot | Inspect interfaces, MAC/IP addresses and routes |
| 2 | ARP analysis | ip neigh, ping, tcpdump, Wireshark | Understand IPv4 neighbour resolution |
| 3 | ICMP analysis | ping, tcpdump, Wireshark | Analyse Echo Request/Reply and reachability |
| 4 | TCP analysis | curl, tcpdump, Wireshark | Identify handshake, ports, flags and data |
| 5 | UDP analysis | Python sockets, tcpdump, Wireshark | Inspect connectionless datagrams |

Follow the matching step-by-step guide in `docs/`.

## Quick start
Network baseline:
```bash
python3 scripts/network_snapshot.py
python3 scripts/network_snapshot.py --output results/network_snapshot.txt
```
UDP demo (run in two terminals):
```bash
python3 scripts/udp_server.py
python3 scripts/udp_client.py --message "Ethernet lab test"
```
List network interfaces:
```bash
ip -brief link
```
Capture only on systems and networks you own or are authorised to inspect:
```bash
sudo bash scripts/capture_traffic.sh lo udp 20
sudo bash scripts/capture_traffic.sh <interface> arp 20
sudo bash scripts/capture_traffic.sh <interface> icmp 20
sudo bash scripts/capture_traffic.sh <interface> tcp 30
```
Open the generated capture with Wireshark:
```bash
wireshark captures/<capture-file>.pcap
```

## Wireshark display filters
| Purpose | Filter |
|---|---|
| ARP | `arp` |
| ICMP | `icmp` |
| TCP | `tcp` |
| UDP | `udp` |
| UDP test port | `udp.port == 5005` |
| TCP SYN | `tcp.flags.syn == 1` |

## Results and screenshots
Store terminal outputs and measured observations in `results/`, reviewed packet captures in `captures/`, and screenshots taken during your own experiments in `screenshots/`. Suggested names:
- `01_network_interfaces.png`
- `02_arp_request_reply.png`
- `03_icmp_echo_packets.png`
- `04_tcp_handshake.png`
- `05_udp_client_server.png`

Network addresses, interface names, ports, sequence numbers, TTL values, timings and packet counts depend on the host and network. Record actual values from your own runs. Do not describe an experiment as completed until you have run it.

## Safety and privacy
Capture only your own device, an isolated lab, or a network for which you have explicit permission. Packet captures can expose IP addresses, hostnames, DNS queries and other metadata; review them before publishing.

## Completion checklist
- [ ] Install required Linux tools.
- [ ] Run and save the network baseline.
- [ ] Perform ARP and record request/reply fields.
- [ ] Perform ICMP and record Echo packet details.
- [ ] Perform TCP and identify a handshake if present.
- [ ] Run UDP client/server and capture datagrams.
- [ ] Add your own screenshots.
- [ ] Complete `docs/report-template.md` using measured results.
- [ ] Review captures for sensitive information before committing.
