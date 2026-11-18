# Experiment 1 — Network interface and addressing baseline

## Aim
Inspect active interfaces, link-layer addresses, assigned IP addresses and routing configuration.

## Commands
```bash
ip -brief link
ip -brief address
ip route
ip neigh
python3 scripts/network_snapshot.py
```

## Procedure
1. Identify the active Ethernet or Wi-Fi interface.
2. Record its interface name, state, MAC address and IPv4/IPv6 addresses.
3. Identify the default route and gateway, if present.
4. Record the neighbour table before and after contacting a local gateway.
5. Save the snapshot output under `results/`.

## Observation sheet
| Field | Your observation |
|---|---|
| Date and time | |
| Operating system | |
| Active interface | |
| MAC address | |
| IPv4 address/prefix | |
| Default gateway | |
| DNS resolver (if checked) | |

## Questions
- What is the role of a MAC address?
- What is the difference between an IP address and a MAC address?
- What does a default route do?

## Conclusion
Write a conclusion based on the configuration observed on your own machine.
