# ChessClient
# Aleksis Vanags
# 13/11/2021

import socket
import threading
import json
import pygame

FORMAT = "utf-8"
PORT = 5050
# Change this to the Server IP
SERVER = "192.168.1.101"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

WIDTH = 400
HEIGHT = 400
SQUARE_SIZE = HEIGHT // 8
FPS = 30
IMAGES = {}

board = []


def main():
    """
    Starts the program when run directly.
    :return: None
    """
    pygame.init()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((255, 255, 255))

    loadImages()

    running = True
    firstClick = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                if firstClick:
                    cStart = location[0] // SQUARE_SIZE
                    rStart = location[1] // SQUARE_SIZE
                else:
                    cEnd = location[0] // SQUARE_SIZE
                    rEnd = location[1] // SQUARE_SIZE
                    MESSAGE = [rStart, cStart, rEnd, cEnd]
                    send(json.dumps(MESSAGE))
                firstClick = not firstClick

        updateBoard(SCREEN)
        CLOCK.tick(FPS)
        pygame.display.flip()


def loadImages():
    """
    Loads the required images into a dictionary when called.
    :return: None
    """
    pieces = ["wP", "wR", "wB", "wQ", "wN", "wK", "bP", "bR", "bB", "bQ", "bN", "bK"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def updateBoard(screen):
    """
    This calls the functions that draw the board and the pieces.
    :param: screen : This is the object the the GUI is running on.
    :return: None
    """
    drawBoard(screen)
    drawPieces(screen)


def drawBoard(screen):
    """
    This draws the baord every time it is called.
    :param: screen : This is the object the the GUI is running on.
    :return: None
    """
    colors = [pygame.Color("white"), pygame.Color("grey")]
    for r in range(8):
        for c in range(8):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen):
    """
    This draws the pieces onto the board every time it is called.
    :param: screen : This is the object the the GUI is running on.
    :return: None
    """
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != "-":
                screen.blit(IMAGES[piece], pygame.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def send(msg):
    """
    This sends a message to the server.
    :param: msg : This is the message that needs to be sent.
    :return: None
    """
    client.send(msg.encode(FORMAT))


def recieve_board():
    """
    This recieves the current board state from the server.
    :return: None
    """
    while True:
        global board # skipcq
        msg = client.recv(368).decode(FORMAT)
        board = json.loads(msg)


if __name__ == "__main__":
    thread = threading.Thread(target=recieve_board)
    thread.start()
    main()
