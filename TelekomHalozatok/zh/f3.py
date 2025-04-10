from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import struct
import select
import sys
import random

bind_address = ''
bind_port = 12000
server_addr = (bind_address, bind_port)

max_numbers = 5
numbers = []
unpacker = struct.Struct('3s i')
packer = struct.Struct('?') 
avg_packer = struct.Struct('f')

with socket(AF_INET, SOCK_STREAM) as server:
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(server_addr)
    server.listen(5)
    print(f"Szerver elindult {bind_address}:{bind_port} címen, várja a klienseket...")
    
    inputs = [server]
    outputs = []
    
    while True:
        r, w, e = select.select(inputs, outputs, inputs)

        for s in r:
            if s is server:
                client, client_addr = server.accept()
                print(f"Új kapcsolat: {client_addr}")
                inputs.append(client)
            else:
                data = s.recv(1024)
                if data:
                    command, value = unpacker.unpack(data)
                    command = command.decode('utf-8').strip()

                    if command == 'PUT':
                        if len(numbers) < max_numbers:
                            numbers.append(value)
                            response = packer.pack(True)
                        else:
                            response = packer.pack(False)

                    elif command == 'REM':
                        if numbers:
                            numbers.pop()
                            response = packer.pack(True)
                        else:
                            response = packer.pack(False)

                    elif command == 'AVG':
                        if numbers:
                            avg = sum(numbers) / len(numbers)
                            response = avg_packer.pack(avg)
                        else:
                            response = avg_packer.pack(0.0)

                    else:
                        response = packer.pack(False)

                    s.send(response)
                else:
                    inputs.remove(s)
                    s.close()

        for s in e:
            inputs.remove(s)
            s.close()
        

    