from socket import socket, AF_INET, SOCK_DGRAM
import struct
import sys

# Server setup
bind_address = sys.argv[1]
bind_port = int(sys.argv[2])
server_addr = (bind_address, bind_port)

unpacker = struct.Struct('c I')
packer = struct.Struct('c I')

with socket(AF_INET, SOCK_DGRAM) as server:
    server.bind(server_addr)
    print(f"UDP Server started at {bind_address}:{bind_port}, waiting for messages...")

    while True:
        data, client_addr = server.recvfrom(unpacker.size)
        print(f"Received connection from {client_addr}")
        
        # TODO: Process received data and implement game logic here
        
        response = packer.pack('X'.encode(), 0)  # Placeholder response
        server.sendto(response, client_addr)