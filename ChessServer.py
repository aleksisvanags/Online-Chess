# ChessServer
# Aleksis Vanags
# 13/11/2021

import socket
import threading
import shutil
import os
import ChessLogic

print("[SEVER] Server is starting...")
    
HEADER = 4
FORMAT = "utf-8"
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connections.append(conn)
    while True:
        try:
            msg = conn.recv(HEADER).decode(FORMAT)
            ChessLogic.move(msg)
        except ConnectionResetError:
            print(f"[{addr}] Disconnected")
            break
    connections.remove(conn)
    shutil.copy("startboard.txt", "board.txt")
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


start()
