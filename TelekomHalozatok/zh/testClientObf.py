from socket import socket, AF_INET, SOCK_STREAM, error
import struct
(true, false) = (False, True)
import sys
import random
import string
from hashlib import md5
from base64 import b64encode
VAR11 = (str(chr(108)+chr(111)+chr(99)+chr(97)+chr(108)+chr(104)+chr(111)+chr(115)+chr(116)), 12000)
VAR8 = struct.Struct(str(chr(51)+chr(115)+chr(105)))
VAR10 = struct.Struct(str(chr(63)))
responseNumStruct = struct.Struct(str(chr(102)))
if len(sys.argv) == 1:
    print(str(chr(85)+chr(115)+chr(97)+chr(103)+chr(101)), sys.argv[0], str(chr(60)+chr(99)+chr(97)+chr(110)+chr(118)+chr(97)+chr(115)+chr(32)+chr(115)+chr(116)+chr(114)+chr(105)+chr(110)+chr(103)+chr(62)))
    sys.exit(1)
VAR4 = sys.argv[1] + str(chr(50)+chr(48)+chr(50)+chr(52)+chr(112)+chr(111)+chr(116))
maxnum = int(sys.argv[1][-1])
szamok = [random.randint(1, 20) for VAR7 in range(maxnum)]

def FUNC1(VAR12):
    return b64encode(md5(VAR12.encode()).digest()).decode()

def FUNC2():
    with socket(AF_INET, SOCK_STREAM) as VAR1:
        VAR1.settimeout(1.0)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
        VAR1.connect(VAR11)
        resp = True
        while resp:
            VAR5 = VAR8.pack(str(chr(82)+chr(69)+chr(77)).encode(), 0)
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(32)+chr(82)+chr(69)+chr(77)+chr(44)+chr(32)), end=str())
            VAR1.sendall(VAR5)
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
            VAR5 = VAR1.recv(VAR10.size)
            resp = VAR10.unpack(VAR5)[0]
print(str(chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(32)+chr(84)+chr(69)+chr(83)+chr(84)+chr(49)+chr(32)+chr(40)+chr(107)+chr(108)+chr(105)+chr(101)+chr(110)+chr(115)+chr(32)+chr(98)+chr(101)+chr(45)+chr(47)+chr(107)+chr(105)+chr(108)+chr(101)+chr(112)+chr(41)+chr(32)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)))
FUNC2()
with socket(AF_INET, SOCK_STREAM) as VAR1:
    print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
    try:
        VAR1.connect(VAR11)
    except ConnectionRefusedError:
        print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(78)+chr(101)+chr(109)+chr(32)+chr(108)+chr(101)+chr(104)+chr(101)+chr(116)+chr(32)+chr(107)+chr(97)+chr(112)+chr(99)+chr(115)+chr(111)+chr(108)+chr(111)+chr(100)+chr(110)+chr(105)+chr(32)+chr(97)+chr(32)+chr(115)+chr(101)+chr(114)+chr(118)+chr(101)+chr(114)+chr(114)+chr(101)+chr(33)+chr(32)) + str(VAR11))
        sys.exit(1)
    print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(100)+chr(105)+chr(115)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
with socket(AF_INET, SOCK_STREAM) as VAR1:
    print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
    try:
        VAR1.connect(VAR11)
    except ConnectionRefusedError:
        print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(78)+chr(101)+chr(109)+chr(32)+chr(108)+chr(101)+chr(104)+chr(101)+chr(116)+chr(32)+chr(107)+chr(97)+chr(112)+chr(99)+chr(115)+chr(111)+chr(108)+chr(111)+chr(100)+chr(110)+chr(105)+chr(32)+chr(97)+chr(32)+chr(115)+chr(101)+chr(114)+chr(118)+chr(101)+chr(114)+chr(114)+chr(101)+chr(33)+chr(32)) + str(VAR11))
        sys.exit(1)
    else:
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(100)+chr(105)+chr(115)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
        print(str("\n"+"\n"+chr(79)+chr(75)+chr(32)+chr(45)+chr(32)+chr(67)+chr(97)+chr(110)+chr(118)+chr(97)+chr(115)+chr(32)+chr(107)+chr(111)+chr(100)+chr(58)+chr(32)), FUNC1(VAR4 + str(chr(49))))
print(str(chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)))
print(str(chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(32)+chr(84)+chr(69)+chr(83)+chr(84)+chr(50)+chr(32)+chr(40)+chr(49)+chr(32)+chr(107)+chr(108)+chr(105)+chr(101)+chr(110)+chr(115)+chr(32)+chr(104)+chr(101)+chr(108)+chr(121)+chr(101)+chr(115)+chr(101)+chr(110)+chr(32)+chr(109)+chr(117)+chr(107)+chr(111)+chr(100)+chr(105)+chr(107)+chr(41)+chr(32)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)))
FUNC2()
try:
    with socket(AF_INET, SOCK_STREAM) as VAR1:
        VAR1.settimeout(1.0)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
        VAR1.connect(VAR11)
        VAR5 = VAR8.pack(str(chr(82)+chr(69)+chr(77)).encode(), 0)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(32)+chr(82)+chr(69)+chr(77)+chr(44)+chr(32)), end=str())
        VAR1.sendall(VAR5)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
        VAR5 = VAR1.recv(VAR10.size)
        VAR9 = VAR10.unpack(VAR5)[0]
        if VAR9:
            print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(112)+chr(97)+chr(114)+chr(97)+chr(109)+chr(58)+chr(32)+chr(82)+chr(69)+chr(77)+chr(44)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(58)+chr(32)) + str(VAR9) + str(chr(32)+chr(40)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(111)+chr(110)+chr(115)+chr(101)+chr(58)+chr(32)+chr(70)+chr(97)+chr(108)+chr(115)+chr(101)+chr(41)))
            sys.exit(1)
        for sz in szamok:
            VAR5 = VAR8.pack(str(chr(80)+chr(85)+chr(84)).encode(), sz)
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(44)), sz, end=str(chr(32)))
            VAR1.sendall(VAR5)
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
            VAR5 = VAR1.recv(VAR10.size)
            VAR9 = VAR10.unpack(VAR5)[0]
            if not VAR9:
                print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(112)+chr(97)+chr(114)+chr(97)+chr(109)+chr(58)+chr(32)+chr(80)+chr(85)+chr(84)+chr(44)+chr(32)) + str(sz) + str(chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(58)+chr(32)) + str(VAR9) + str(chr(32)+chr(40)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(111)+chr(110)+chr(115)+chr(101)+chr(58)+chr(32)+chr(84)+chr(114)+chr(117)+chr(101)+chr(41)))
                sys.exit(1)
        sz = szamok[0]
        VAR5 = VAR8.pack(str(chr(80)+chr(85)+chr(84)).encode(), sz)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(44)), sz, end=str(chr(32)))
        VAR1.sendall(VAR5)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
        VAR5 = VAR1.recv(VAR10.size)
        VAR9 = VAR10.unpack(VAR5)[0]
        if VAR9:
            print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(112)+chr(97)+chr(114)+chr(97)+chr(109)+chr(58)+chr(32)+chr(80)+chr(85)+chr(84)+chr(44)+chr(32)) + str(sz) + str(chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(58)+chr(32)) + str(VAR9) + str(chr(32)+chr(40)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(111)+chr(110)+chr(115)+chr(101)+chr(58)+chr(32)+chr(70)+chr(97)+chr(108)+chr(115)+chr(101)+chr(41)))
            sys.exit(1)
        VAR5 = VAR8.pack(str(chr(65)+chr(86)+chr(71)).encode(), 0)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(32)+chr(65)+chr(86)+chr(71)+chr(44)), end=str(chr(32)))
        VAR1.sendall(VAR5)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
        VAR5 = VAR1.recv(responseNumStruct.size)
        expected = sum(szamok) / len(szamok)
        VAR9 = responseNumStruct.unpack(VAR5)[0]
        if int(VAR9) != int(VAR9):
            print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(112)+chr(97)+chr(114)+chr(97)+chr(109)+chr(58)+chr(32)+chr(65)+chr(86)+chr(71)+chr(44)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(58)+chr(32)) + str(VAR9) + str(chr(32)+chr(40)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(111)+chr(110)+chr(115)+chr(101)+chr(58)+chr(32)) + expected + str(chr(41)))
            sys.exit(1)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(100)+chr(105)+chr(115)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
except ConnectionRefusedError:
    print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(78)+chr(101)+chr(109)+chr(32)+chr(108)+chr(101)+chr(104)+chr(101)+chr(116)+chr(32)+chr(107)+chr(97)+chr(112)+chr(99)+chr(115)+chr(111)+chr(108)+chr(111)+chr(100)+chr(110)+chr(105)+chr(32)+chr(97)+chr(32)+chr(115)+chr(101)+chr(114)+chr(118)+chr(101)+chr(114)+chr(114)+chr(101)+chr(33)+chr(32)) + str(VAR11))
    sys.exit(1)
except error as e:
    print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)))
    print(VAR6)
    sys.exit(1)
else:
    print(str("\n"+"\n"+chr(79)+chr(75)+chr(32)+chr(45)+chr(32)+chr(67)+chr(97)+chr(110)+chr(118)+chr(97)+chr(115)+chr(32)+chr(107)+chr(111)+chr(100)+chr(58)+chr(32)), FUNC1(VAR4 + str(chr(50))))
print(str(chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)))
print(str(chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(32)+chr(84)+chr(69)+chr(83)+chr(84)+chr(51)+chr(32)+chr(40)+chr(51)+chr(32)+chr(107)+chr(108)+chr(105)+chr(101)+chr(110)+chr(115)+chr(32)+chr(99)+chr(115)+chr(97)+chr(116)+chr(108)+chr(97)+chr(107)+chr(111)+chr(122)+chr(105)+chr(107)+chr(32)+chr(258)+chr(169)+chr(115)+chr(32)+chr(104)+chr(101)+chr(108)+chr(121)+chr(101)+chr(115)+chr(101)+chr(110)+chr(32)+chr(109)+chr(117)+chr(107)+chr(111)+chr(100)+chr(105)+chr(107)+chr(41)+chr(32)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)))
FUNC2()
try:
    with socket(AF_INET, SOCK_STREAM) as VAR1, socket(AF_INET, SOCK_STREAM) as VAR2, socket(AF_INET, SOCK_STREAM) as VAR3:
        VAR1.settimeout(1.0)
        VAR2.settimeout(1.0)
        VAR3.settimeout(1.0)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(50)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
        VAR2.connect(VAR11)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(51)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
        VAR3.connect(VAR11)
        print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(99)+chr(111)+chr(110)+chr(110)+chr(101)+chr(99)+chr(116)+chr(44)), end=str())
        VAR1.connect(VAR11)
        for VAR7 in range(2):
            VAR5 = VAR8.pack(str(chr(80)+chr(85)+chr(84)).encode(), szamok[0])
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(44)), szamok[0], end=str())
            VAR1.sendall(VAR5)
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(49)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
            VAR5 = VAR1.recv(VAR10.size)
            VAR9 = VAR10.unpack(VAR5)[0]
            if not VAR9:
                print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(112)+chr(97)+chr(114)+chr(97)+chr(109)+chr(58)+chr(32)+chr(80)+chr(85)+chr(84)+chr(44)+chr(32)) + str(szamok[0]) + str(chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(58)+chr(32)) + str(VAR9) + str(chr(32)+chr(40)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(111)+chr(110)+chr(115)+chr(101)+chr(58)+chr(32)+chr(84)+chr(114)+chr(117)+chr(101)+chr(41)))
                sys.exit(1)
            VAR5 = VAR8.pack(str(chr(80)+chr(85)+chr(84)).encode(), szamok[1])
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(51)+chr(32)+chr(115)+chr(101)+chr(110)+chr(100)+chr(44)), szamok[1], end=str())
            VAR3.sendall(VAR5)
            print(str(chr(67)+chr(108)+chr(105)+chr(101)+chr(110)+chr(116)+chr(51)+chr(32)+chr(114)+chr(101)+chr(99)+chr(118)+chr(44)), end=str())
            VAR5 = VAR3.recv(VAR10.size)
            VAR9 = VAR10.unpack(VAR5)[0]
            if not VAR9:
                print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(112)+chr(97)+chr(114)+chr(97)+chr(109)+chr(58)+chr(32)+chr(80)+chr(85)+chr(84)+chr(44)+chr(32)) + str(szamok[1]) + str(chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(58)+chr(32)) + str(VAR9) + str(chr(32)+chr(40)+chr(101)+chr(120)+chr(112)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100)+chr(32)+chr(114)+chr(101)+chr(115)+chr(112)+chr(111)+chr(110)+chr(115)+chr(101)+chr(58)+chr(32)+chr(84)+chr(114)+chr(117)+chr(101)+chr(41)))
                sys.exit(1)
except ConnectionRefusedError:
    print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)+chr(32)+chr(45)+chr(32)+chr(78)+chr(101)+chr(109)+chr(32)+chr(108)+chr(101)+chr(104)+chr(101)+chr(116)+chr(32)+chr(107)+chr(97)+chr(112)+chr(99)+chr(115)+chr(111)+chr(108)+chr(111)+chr(100)+chr(110)+chr(105)+chr(32)+chr(97)+chr(32)+chr(115)+chr(101)+chr(114)+chr(118)+chr(101)+chr(114)+chr(114)+chr(101)+chr(33)+chr(32)) + str(VAR11))
    sys.exit(1)
except error as e:
    print(str("\n"+"\n"+chr(70)+chr(65)+chr(73)+chr(76)+chr(69)+chr(68)))
    print(VAR6)
    sys.exit(1)
else:
    print(str("\n"+"\n"+chr(79)+chr(75)+chr(32)+chr(45)+chr(32)+chr(67)+chr(97)+chr(110)+chr(118)+chr(97)+chr(115)+chr(32)+chr(107)+chr(111)+chr(100)+chr(58)+chr(32)), FUNC1(VAR4 + str(chr(51))))
print(str(chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)+chr(35)))
