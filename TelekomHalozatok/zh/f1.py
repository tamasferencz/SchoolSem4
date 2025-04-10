import socket 
import time
import struct

NEPTUN_ID = "g0820e"
SECRET = "2vj992t2d53em2v5"
SERVER_IP = "oktnb147.inf.elte.hu"
SERVER_PORT = 11224

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(20)

session_packer = struct.Struct('10s 6s 20s')
session_message = session_packer.pack(b"UDPStart", NEPTUN_ID.encode(), SECRET.encode())

client_socket.sendto(session_message, (SERVER_IP, SERVER_PORT))

response, _ = client_socket.recvfrom(1024)
response_unpacker = struct.Struct('10s 100s')
response_data = response_unpacker.unpack(response)
response_code, session_id = response_data

if response_code.decode() == "OK":
    time.sleep(1)

    stop_packer = struct.Struct('10s 25s')
    stop_message = stop_packer.pack(b"UDPStop", session_id.strip().encode())
    client_socket.sendto(stop_message, (SERVER_IP, SERVER_PORT))

    response, _ = client_socket.recvfrom(1024)
    response_data = response_unpacker.unpack(response)
    result_code, result_message = response_data
    print(f"Response: {result_code.decode()}, Message: {result_message.decode().strip()}")
