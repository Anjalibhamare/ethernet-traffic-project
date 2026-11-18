# Experiment 5 — UDP client/server traffic

## Aim
Generate local UDP datagrams and inspect their headers and payload in Wireshark.

## Procedure
1. Terminal 1: `python3 scripts/udp_server.py`.
2. Terminal 2: `sudo bash scripts/capture_traffic.sh lo udp 20`.
3. During capture, terminal 3: `python3 scripts/udp_client.py --message "test datagram"`.
4. Open the saved capture and apply `udp.port == 5005`.
5. Record source/destination ports, UDP length and payload.

## Observation sheet
| Item | Observed value |
|---|---|
| Source address/port | |
| Destination address/port | |
| UDP length | |
| Payload | |
| Server response | |

## Analysis
UDP is connectionless and does not provide built-in delivery, ordering or retransmission guarantees. The example server sends an application-level acknowledgement; that does not make UDP itself reliable.

## Questions
- Why is UDP described as connectionless?
- What fields are present in a UDP header?
- Give two applications that may use UDP.

## Conclusion
Summarise the datagram exchange seen in your own terminal and packet capture.
