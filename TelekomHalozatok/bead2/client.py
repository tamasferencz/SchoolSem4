import struct
import sys

def read_first_record(file_path, format):
    with open(file_path, 'rb') as file:
        record_size = struct.calcsize(format)
        record_data = file.read(record_size)
        unpacked_data = struct.unpack(format, record_data)
        return unpacked_data
    
def task1(file1,file2,file3,file4):
    format1 = 'if?'
    format2 = '?c9s'
    format3 = '9sfi'
    format4 = '?ic'
    
    record1 = read_first_record(file1, format1)
    record2 = read_first_record(file2, format2)
    record3 = read_first_record(file3, format3)
    record4 = read_first_record(file4, format4)
    
    if record1:
        print(record1)
    if record2:
        print(record2)
    if record3:
        print(record3)
    if record4:
        print(record4)

def task2():
    
    packed1 = struct.pack('18s i ?', b'elso', 48, True)
    packed2 = struct.pack('f ? c', 51.5, False, b'X')
    packed3 = struct.pack('i 16s f', 39, b'masodik', 58.9)
    packed4 = struct.pack('c i 19s', b'Z', 70, b'harmadik')
    
    print(packed1)
    print(packed2)
    print(packed3)
    print(packed4)

def main():
    if len(sys.argv) != 5:
        print("Használat: python3 client.py <file1> <file2> <file3> <file4>")
        sys.exit(1)
        
    file1,file2,file3,file4 = sys.argv[1:5]
    task1(file1,file2,file3,file4)
    
    task2()

if __name__ == "__main__":
    main()