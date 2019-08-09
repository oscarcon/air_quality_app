#!/usr/bin/env python3

import socket
import threading



HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 12345        # Port to listen on (non-privileged ports are > 1023)

def client_handler(sock_conn):
    with sock_conn:
        while True:
            data = sock_conn.recv(1024)
            print(data)
    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        threading.Thread(target=client_handler, args=(conn,)).start()  
    # with conn:
    #     while True:
    #         data = conn.recv(1024)
    #         print(data)
    #         if not data:
    #             break
    #         conn.sendall(data)