#!/usr/bin/env python3
"""Send a UDP datagram to the local experiment server and display its response."""
import argparse, socket

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host',default='127.0.0.1'); parser.add_argument('--port',type=int,default=5005)
    parser.add_argument('--message',default='Ethernet traffic analysis lab'); parser.add_argument('--timeout',type=float,default=3.0)
    args=parser.parse_args()
    if not 1<=args.port<=65535: parser.error('--port must be between 1 and 65535')
    if args.timeout<=0: parser.error('--timeout must be positive')
    payload=args.message.encode('utf-8')
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client:
            client.settimeout(args.timeout); client.sendto(payload,(args.host,args.port))
            print(f'Sent {len(payload)} bytes to {args.host}:{args.port}')
            response,peer=client.recvfrom(4096)
            print(f'Received {len(response)} bytes from {peer}: {response.decode("utf-8",errors="replace")}')
    except socket.timeout: print('No response before timeout. Check that the UDP server is running.'); return 2
    except OSError as exc: print(f'UDP client error: {exc}'); return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
