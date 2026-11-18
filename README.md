# Ethernet Network Monitoring and Traffic Analysis

An independently developed Linux networking lab project for studying Ethernet interfaces, IPv4 configuration, ARP, ICMP, TCP and UDP traffic with command-line tools and Wireshark.

## Learning goals
- Inspect network interfaces, MAC addresses, IPv4 addresses and routes.
- Observe ARP neighbour discovery and ICMP reachability tests.
- Capture TCP handshakes and UDP datagrams.
- Generate a controlled local UDP client/server exchange.
- Preserve packet captures and record observations reproducibly.

## Repository layout
```text
.
├── README.md
├── requirements.txt
├── docs/
│   ├── 01-network-baseline.md
│   ├── 02-arp-study.md
│   ├── 03-icmp-study.md
│   ├── 04-tcp-study.md
│   └── 05-udp-study.md
├── scripts/
│   ├── network_snapshot.py
│   ├── udp_server.py
│   ├── udp_client.py
│   └── capture_traffic.sh
├── results/       # Save your own command output here
└── captures/      # Save your own .pcapng files here
```

## Requirements
- Linux (Ubuntu, Debian, Pop!_OS or equivalent)
- Python 3.9+
- Wireshark or tshark
- tcpdump (for packet capture)
- ping and standard iproute2 utilities

Install optional Python dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick start
1. Inspect the host: `python3 scripts/network_snapshot.py`
2. Read the experiment guides in `docs/`.
3. For UDP, open one terminal and run `python3 scripts/udp_server.py`.
4. In another terminal run `python3 scripts/udp_client.py --message "Ethernet lab test"`.
5. Capture traffic only on an interface and network you are authorised to inspect:
   `sudo bash scripts/capture_traffic.sh lo udp`

Open a capture with `wireshark captures/udp.pcap`. Useful display filters:
- ARP: `arp`
- ICMP: `icmp`
- TCP: `tcp`
- UDP: `udp`
- UDP test port: `udp.port == 5005`

## Evidence and reporting
Store your own terminal outputs in `results/` and packet captures in `captures/`. The experiment guides include observation tables. Fill them from your actual machine and packet captures; network addresses, ports, timings and packet counts vary by environment. Do not treat example commands as measured results.

## Safety
Capture only your own device, a lab network, or traffic for which you have explicit permission. Packet captures can contain sensitive information; review them before publishing.

## Project status
This repository provides the scripts and reproducible experiment workflow. Add dated screenshots, captures and measured observations after running the experiments on your system.
