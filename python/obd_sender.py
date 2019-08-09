import socket
import time

# while True:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('192.168.43.155', 35000))
    for i in range(0,32):
        cmd = "%02x" % i
        cmd = '01 ' + cmd + '\r'
        cmd = cmd.encode()
        sock.send(cmd)
        print('respond: ', sock.recv(128))
        time.sleep(0.2)
# time.sleep(0.01)
