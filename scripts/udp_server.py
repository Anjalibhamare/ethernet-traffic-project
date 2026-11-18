#!/usr/bin/env python3
"""Small UDP echo server for a controlled localhost experiment."""
import argparse
import socket

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Bind address (default: localhost)")
    parser.add_argument("--port", type=int, default=5005)
    parser.add_argument("--max-messages", type=int, default=0, help="0 means run until Ctrl+C")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")
    count = 0
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind((args.host, args.port))
        print(f"Listening on {args.host}:{args.port}; press Ctrl+C to stop")
        try:
            while not args.max_messages or count < args.max_messages:
                payload, peer = server.recvfrom(4096)
                message = payload.decode("utf-8", errors="replace")
                print(f"Received {len(payload)} bytes from {peer}: {message}")
                server.sendto(b"ACK: " + payload, peer)
                count += 1
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
