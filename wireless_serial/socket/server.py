#!/usr/bin/env python3
import time
import socket
from pynput.keyboard import Key, Listener



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1234        # Port to listen on (non-privileged ports are > 1023)




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        def on_press(key):
            return
        def on_release(key):
            try:
                conn.send(str(key.char).encode())
                print("Send " + key.char)
            except socket.error as e:
                print(e)
            except:
                print("Modifier Key")
                pass
        with Listener(on_press=on_press, on_release=on_release) as listener:
            while True:
                data = conn.recv(1024)
                print(str(data))
                # if not data:
                #     break
                # conn.sendall(data)
                #onn.sendall(b'Hello World\r\n')
                #time.sleep(1)
            listener.join()
    s.close()