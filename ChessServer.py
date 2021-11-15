# ChessServer
# Aleksis Vanags
# 13/11/2021

import socket
import threading
import os
import json
import ChessLogic

print("[SEVER] Server is starting...")
    
HEADER = 12
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
    conn.send(json.dumps(ChessLogic.board).encode(FORMAT))
    while True:
        try:
            msg = conn.recv(HEADER).decode(FORMAT)
            print(msg)
            board = ChessLogic.move(msg)
            if board != None:
                board = board.encode(FORMAT)
                for conn in connections:
                    conn.send(board)
        except ConnectionResetError:
            print(f"[{addr}] Disconnected")
            break
        except Exception as e:
            print(f"oh, this is weird\n{e}")
    for conn in connections:
        conn.close()
        connections.remove(conn)


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


start()
