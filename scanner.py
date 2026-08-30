import socket

target = "192.168.1.3"

for port in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((target,port))
        print(f"{port}/tcp OPEN")
    except socket.error:
        pass
    finally:
        s.close()