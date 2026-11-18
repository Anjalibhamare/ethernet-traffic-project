#!/usr/bin/env python3
"""Local UDP echo server for the UDP traffic experiment."""
import argparse, socket

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host',default='127.0.0.1',help='Bind address (localhost by default)')
    parser.add_argument('--port',type=int,default=5005)
    parser.add_argument('--max-messages',type=int,default=0,help='Stop after N datagrams; 0 runs until Ctrl+C')
    args=parser.parse_args()
    if not 1<=args.port<=65535: parser.error('port must be between 1 and 65535')
    if args.max_messages<0: parser.error('--max-messages cannot be negative')
    count=0
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server:
            server.bind((args.host,args.port)); print(f'UDP server listening on {args.host}:{args.port}; Ctrl+C to stop')
            while args.max_messages==0 or count<args.max_messages:
                payload,peer=server.recvfrom(4096)
                print(f'Datagram {count+1}: {len(payload)} bytes from {peer}: {payload.decode("utf-8",errors="replace")}')
                server.sendto(b'ACK: '+payload,peer); count+=1
    except KeyboardInterrupt: print('\nServer stopped by user.')
    except OSError as exc: print(f'UDP server error: {exc}'); return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
