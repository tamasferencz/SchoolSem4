from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import struct
import time
import random
import select
import sys

bind_address = sys.argv[1]
bind_port = int(sys.argv[2])
server_addr = (bind_address, bind_port)

unpacker = struct.Struct('c I')
packer = struct.Struct('c I')

with socket(AF_INET, SOCK_STREAM) as server:
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(server_addr)
    server.listen(5)
    print(f"Szerver elindult {bind_address}:{bind_port} címen, várja a klienseket...")

    inputs = [server]
    clients = {}
    number = random.randint(1, 100)
    game_over = False

    while True:
        readable, _, _ = select.select(inputs, [], [], 1.0)

        for s in readable:
            if s is server:
                client, client_addr = server.accept()
                print(f"Csatlakozott: {client_addr}")
                inputs.append(client)
                clients[client] = {"state": None, "address": client_addr}
            else:
                try:
                    data = s.recv(unpacker.size)
                    if not data:
                        inputs.remove(s)
                        s.close()
                        del clients[s]
                        continue

                    op, guess = unpacker.unpack(data)
                    op = op.decode()

                    if game_over:
                        s.sendall(packer.pack('V'.encode(), 0))
                        continue

                    if op == '=':
                        if guess == number:
                            clients[s]["state"] = 'Y'
                            s.sendall(packer.pack('Y'.encode(), 0))
                            game_over = True
                        else:
                            clients[s]["state"] = 'N'
                            s.sendall(packer.pack('N'.encode(), 0))
                    elif op == '<':
                        response = 'I' if number < guess else 'N'
                        clients[s]["state"] = response
                        s.sendall(packer.pack(response.encode(), 0))
                    elif op == '>':
                        response = 'I' if number > guess else 'N'
                        clients[s]["state"] = response
                        s.sendall(packer.pack(response.encode(), 0))

                except (ConnectionError, struct.error):
                    inputs.remove(s)
                    s.close()
                    del clients[s]

        if game_over:
            for s in inputs[1:]:
                    if clients[s]["state"] != 'Y':
                        s.sendall(packer.pack('K'.encode(), 0))
                    else:
                        s.sendall(packer.pack('V'.encode(),0))
            inputs = [server]
            clients.clear()
            number = random.randint(1, 100)
            game_over = False
            print(f"Új játék kezdődik, a szám: {number}")
