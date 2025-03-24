from socket import socket, AF_INET, SOCK_STREAM
import struct
import sys
import time
import random
import select

server_addr = (sys.argv[1], int(sys.argv[2]))
packer = struct.Struct('c I')
unpacker = struct.Struct('c I')

low = 1
high = 100

with socket(AF_INET, SOCK_STREAM) as client:
    client.connect(server_addr)
    client.settimeout(5.0)

    while low <= high:
        mid = (low + high) // 2
        print(f"Tippelt szám: {mid}")

        time.sleep(random.uniform(1, 5))

        packed_data = packer.pack('='.encode(), mid)
        client.sendall(packed_data)

        readable, _, _ = select.select([client], [], [], 5.0)
        if not readable:
            print("Hiba: Timeout - nem érkezett válasz a szervertől.")
            break

        response = client.recv(unpacker.size) 
        if not response:
            print("Hiba: A szerver lezárta a kapcsolatot.")
            break

        op, _ = unpacker.unpack(response)
        op = op.decode()

        if op in ['Y', 'K', 'V']:
            print(f"A játék véget ért: {op}")
            client.close()
            break
        elif op == 'N':
            packed_data = packer.pack(('>' if mid < high else '<').encode(), mid)
            client.sendall(packed_data)

            readable, _, _ = select.select([client], [], [], 5.0)
            response = client.recv(unpacker.size)
            op, _ = unpacker.unpack(response)
            op = op.decode()

            if op == 'I':
                low = mid + 1
            else:
                high = mid - 1
