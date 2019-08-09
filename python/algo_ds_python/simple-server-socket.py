import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Successfully create socket")
except:
    print("Failed to create socket")

port = 1234
s.bind(('0.0.0.0', port))

s.listen(5)

while True:
    c, addr = s.accept()
    c.send('Hello from server'.encode())
    c.close()
