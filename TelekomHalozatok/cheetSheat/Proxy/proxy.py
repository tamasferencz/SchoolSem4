from socket import socket, AF_INET, SOCK_DGRAM
import struct
import sys

# Proxy setup
proxy_address = sys.argv[1]
proxy_port = int(sys.argv[2])
server_address = (sys.argv[3], int(sys.argv[4]))

unpacker = struct.Struct('c I')
packer = struct.Struct('c I')

with socket(AF_INET, SOCK_DGRAM) as proxy:
    proxy.bind((proxy_address, proxy_port))
    print(f"UDP Proxy started at {proxy_address}:{proxy_port}, forwarding to {server_address}...")

    while True:
        data, client_addr = proxy.recvfrom(unpacker.size)
        print(f"Received data from {client_addr}, forwarding to server...")
        
        # Forward data to the actual server
        proxy.sendto(data, server_address)
        
        # Receive response from the server
        response, _ = proxy.recvfrom(unpacker.size)
        
        # Send the response back to the client
        proxy.sendto(response, client_addr)
