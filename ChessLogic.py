# ChessLogic
# Aleksis Vanags
# 13/11/2021

import json

board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
         ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
         ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
legalMoves = []
turn = True


def move(userMove):
    global turn
    global board
    checkLegalMoves()
    userMove = [int(x) for x in userMove]
    if "".join(str(i) for i in userMove) in legalMoves:
        board[userMove[2]][userMove[3]] = board[userMove[0]][userMove[1]]
        board[userMove[0]][userMove[1]] = "--"
        legalMoves.clear()
        turn = not turn
    return json.dumps(board)


def checkLegalMoves():
    for r in range(0, 8):
        for c in range(0, 8):
            if board[r][c] == "--":
                pass
            elif board[r][c][0] == "w" and turn:
                if board[r][c][1] == "P":
                    checkPawn(r, c, "w")
                elif board[r][c][1] == "R":
                    checkRook(r, c, "w")
                elif board[r][c][1] == "B":
                    checkBishop(r, c, "w")
                elif board[r][c][1] == "Q":
                    checkQueen(r, c, "w")
                elif board[r][c][1] == "K":
                    checkKing(r, c, "w")
                else:
                    checkKnight(r, c, "w")
            elif board[r][c][0] == "b" and not turn:
                if board[r][c][1] == "P":
                    checkPawn(r, c, "b")
                elif board[r][c][1] == "R":
                    checkRook(r, c, "b")
                elif board[r][c][1] == "B":
                    checkBishop(r, c, "b")
                elif board[r][c][1] == "Q":
                    checkQueen(r, c, "b")
                elif board[r][c][1] == "K":
                    checkKing(r, c, "b")
                else:
                    checkKnight(r, c, "b")



def checkPawn(r, c, color):
    if color == "w":
        if r == 6:
            if board[r - 2][c] == "--" and board[r - 1][c] == "--":
                legalMoves.append(f"{r}{c}{r - 2}{c}")
        if r - 1 >= 0:
            if board[r - 1][c] == "--":
                legalMoves.append(f"{r}{c}{r - 1}{c}")
            if c - 1 >= 0 and board[r - 1][c - 1][0] == "b":
                legalMoves.append(f"{r}{c}{r - 1}{c - 1}")
            if c + 1 <= 7 and board[r - 1][c + 1][0] == "b":
                legalMoves.append(f"{r}{c}{r - 1}{c + 1}")
    if color == "b":
        if r == 1:
            if board[r + 2][c] == "--" and board[r + 1][c] == "--":
                legalMoves.append(f"{r}{c}{r + 2}{c}")
        if r + 1 <= 7:
            if board[r + 1][c] == "--":
                legalMoves.append(f"{r}{c}{r + 1}{c}")
            if c - 1 >= 0 and board[r + 1][c - 1][0] == "w":
                legalMoves.append(f"{r}{c}{r + 1}{c - 1}")
            if c + 1 <= 7 and board[r + 1][c + 1][0] == "w":
                legalMoves.append(f"{r}{c}{r + 1}{c + 1}")
        


def checkRook(r, c, color):
    row = r
    while row > 0:
        row -= 1
        if board[row][c][0] != color:
            legalMoves.append(f"{r}{c}{row}{c}")
            if board[row][c] != "--":
                break
        else:
            break
    row = r
    while row < 7:
        row += 1
        if board[row][c][0] != color:
            legalMoves.append(f"{r}{c}{row}{c}")
            if board[row][c] != "--":
                break
        else:
            break
    col = c
    while col > 0:
        col -= 1
        if board[r][col][0] != color:
            legalMoves.append(f"{r}{c}{r}{col}")
            if board[r][col] != "--":
                break
        else:
            break
    col = c
    while col < 7:
        col += 1
        if board[r][col][0] != color:
            legalMoves.append(f"{r}{c}{r}{col}")
            if board[r][col] != "--":
                break
        else:
            break


def checkBishop(r, c, color):
    row = r
    col = c
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        if board[row][col][0] != color:
            legalMoves.append(f"{r}{c}{row}{col}")
            if board[row][col] != "--":
                break
        else:
            break
    row = r
    col = c
    while row > 0 and col < 7:
        row -= 1
        col += 1
        if board[row][col][0] != color:
            legalMoves.append(f"{r}{c}{row}{col}")
            if board[row][col] != "--":
                break
        else:
            break
    row = r
    col = c
    while row < 7 and col > 0:
        row += 1
        col -= 1
        if board[row][col][0] != color:
            legalMoves.append(f"{r}{c}{row}{col}")
            if board[row][col] != "--":
                break
        else:
            break
    row = r
    col = c
    while row < 7 and col < 7:
        row += 1
        col += 1
        if board[row][col][0] != color:
            legalMoves.append(f"{r}{c}{row}{col}")
            if board[row][col] != "--":
                break
        else:
            break


def checkQueen(r, c, color):
    checkRook(r, c, color)
    checkBishop(r, c, color)


def checkKing(r, c, color):
    pass
    # Create Logic for this


def checkKnight(r, c, color):
    if r - 2 >= 0:
        if c - 1 >= 0:
            if board[r - 2][c - 1][0] != color:
                legalMoves.append(f"{r}{c}{r - 2}{c - 1}")
        if c + 1 <= 7:
            if board[r - 2][c + 1][0] != color:
                legalMoves.append(f"{r}{c}{r - 2}{c + 1}")
    if r + 2 <= 7:
        if c - 1 >= 0:
            if board[r + 2][c - 1][0] != color:
                legalMoves.append(f"{r}{c}{r + 2}{c - 1}")
        if c + 1 <= 7:
            if board[r + 2][c + 1][0] != color:
                legalMoves.append(f"{r}{c}{r + 2}{c + 1}")
    if c - 2 >= 0:
        if r - 1 >= 0:
            if board[r - 1][c - 2][0] != color:
                legalMoves.append(f"{r}{c}{r - 1}{c - 2}")
        if r + 1 <= 7:
            if board[r + 1][c - 2][0] != color:
                legalMoves.append(f"{r}{c}{r + 1}{c - 2}")
    if c + 2 <= 7:
        if r - 1 >= 0:
            if board[r - 1][c + 2][0] != color:
                legalMoves.append(f"{r}{c}{r - 1}{c + 2}")
        if r + 1 <= 7:
            if board[r + 1][c + 2][0] != color:
                legalMoves.append(f"{r}{c}{r + 1}{c + 2}")


def checkProtected(r, c, color):
    pass
    # Rook/Queen Check
    # Bishop/Queen Check
    # Pawn Check
    # Knight Check
    # King Check


