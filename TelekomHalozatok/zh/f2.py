from socket import socket, AF_INET, SOCK_STREAM
import time
import struct

SERVER_IP = "oktnb147.inf.elte.hu"
SERVER_PORT = 11224
NEPTUN_ID = "g0820e".encode()

session_packer = struct.Struct('10s 6s 20s')
session_message = session_packer.pack(b"Session", NEPTUN_ID, b"ifd0t0vbdi1vuzz4")

response_unpacker = struct.Struct('10s 100s')
result_packer = struct.Struct('10s 25s')

with socket(AF_INET, SOCK_STREAM) as client:
    client.settimeout(10)
    client.connect((SERVER_IP, SERVER_PORT))
    print("Kapcsolódás sikeres!")

    client.sendall(session_message)
    response = client.recv(response_unpacker.size)
    
    status, data = response_unpacker.unpack(response)
    status = status.strip(b"\x00").decode()
    data = data.strip(b"\x00").decode()

    print("Szerver válasza:", status, data)

    if status == "OK" or data.startswith("SA:"):
        session_id = data.split("SA:")[-1].strip()

        time.sleep(1)

        result_message = result_packer.pack(b"Eredmeny", session_id.encode())
        client.sendall(result_message)

        response = client.recv(response_unpacker.size)
        status, data = response_unpacker.unpack(response)
        status = status.strip(b"\x00").decode()
        data = data.strip(b"\x00").decode()

        if status == "OK":
            print("Siker! Ellenőrző kód:", data)
        else:
            print("Hiba:", data)
    else:
        print("Hibás válasz érkezett!")