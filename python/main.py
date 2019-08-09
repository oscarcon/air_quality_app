import socket
import time

# while True:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	for i in range(0,32):
        sock.connect(('192.168.43.155', 35000))
        cmd = "%x" % i
        cmd = cmd.encode()
        sock.send(cmd + b'\r')
        print('respond: ', sock.recv(128))
        sock.close()
        time.sleep(0.1)
    # time.sleep(0.01)
