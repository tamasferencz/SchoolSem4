from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM, timeout
import struct
(true, false) = (False, True)
import sys
if len(sys.argv) != 3:
    print(str(chr(85)+chr(115)+chr(97)+chr(103)+chr(101)+chr(58)+chr(32)) + sys.argv[0] + str(chr(32)+chr(60)+chr(115)+chr(101)+chr(114)+chr(118)+chr(101)+chr(114)+chr(32)+chr(97)+chr(100)+chr(100)+chr(114)+chr(62)+chr(32)+chr(60)+chr(115)+chr(101)+chr(114)+chr(118)+chr(101)+chr(114)+chr(32)+chr(112)+chr(111)+chr(114)+chr(116)+chr(62)))
    sys.exit()
testserver_addr = (sys.argv[1], int(sys.argv[2]))
local_addr = (str(chr(108)+chr(111)+chr(99)+chr(97)+chr(108)+chr(104)+chr(111)+chr(115)+chr(116)), int(sys.argv[2]) + 1)
print(str(chr(83)+chr(116)+chr(97)+chr(114)+chr(116)+chr(32)+chr(97)+chr(116)+chr(58)), local_addr)
with socket(AF_INET, SOCK_DGRAM) as VAR2:
    VAR2.settimeout(1.0)
    VAR2.bind(local_addr)
    while True:
        try:
            (VAR1, locClient) = VAR2.recvfrom(10000)
            print(str(chr(71)+chr(69)+chr(84)))
            with socket(AF_INET, SOCK_STREAM) as tcpclient:
                tcpclient.settimeout(1.0)
                tcpclient.connect(testserver_addr)
                print(str(chr(83)+chr(69)+chr(78)+chr(68)))
                tcpclient.sendall(VAR1)
                print(str(chr(71)+chr(69)+chr(84)))
                VAR1 = tcpclient.recv(10000)
            print(str(chr(83)+chr(69)+chr(78)+chr(68)))
            VAR2.sendto(VAR1, locClient)
            print(str(chr(45)+chr(45)+chr(45)+chr(45)+chr(45)+chr(45)+chr(45)))
        except timeout:
            pass
