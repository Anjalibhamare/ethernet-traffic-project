#!/usr/bin/env python3
"""Send a UDP datagram to the lab echo server and print its response."""
import argparse
import socket

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5005)
    parser.add_argument("--message", default="Ethernet traffic analysis lab")
    parser.add_argument("--timeout", type=float, default=3.0)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(args.timeout)
        client.sendto(args.message.encode("utf-8"), (args.host, args.port))
        print(f"Sent {len(args.message.encode('utf-8'))} bytes to {args.host}:{args.port}")
        try:
            response, peer = client.recvfrom(4096)
            print(f"Response from {peer}: {response.decode('utf-8', errors='replace')}")
        except socket.timeout:
            raise SystemExit("No response received before timeout; check that the server is running.")

if __name__ == "__main__":
    main()
