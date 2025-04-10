from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import struct
import select
import sys

# Server setup
bind_address = sys.argv[1]
bind_port = int(sys.argv[2])
server_addr = (bind_address, bind_port)

unpacker = struct.Struct('c I') # char, integer
packer = struct.Struct('c I') # char, integer

with socket(AF_INET, SOCK_STREAM) as server:
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(server_addr)
    server.listen(5)
    print(f"Server started at {bind_address}:{bind_port}, waiting for clients...")

    inputs = [server]
    clients = {}

    while True:
        readable, _, _ = select.select(inputs, [], [], 1.0)

        for s in readable:
            if s is server:
                client, client_addr = server.accept()
                print(f"Connected: {client_addr}")
                inputs.append(client)
                clients[client] = {"address": client_addr}
            else:
                try:
                    data = s.recv(unpacker.size)
                    if not data:
                        inputs.remove(s)
                        s.close()
                        del clients[s]
                        continue
                    
                    # TODO: Process received data and implement game logic here
                    
                    response = packer.pack('X'.encode(), 0)  # Placeholder response
                    s.sendall(response)
                except (ConnectionError, struct.error):
                    inputs.remove(s)
                    s.close()
                    del clients[s]