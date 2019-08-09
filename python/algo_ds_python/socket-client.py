import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    pass
port = 1234

sock.connect(('127.0.0.1',port))

print(sock.recv(1024))

sock.close()
