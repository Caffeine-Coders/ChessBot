from copy import deepcopy

import chess

#============================================ white eval
Wpawneval = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
    [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
    [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
knighteval = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]
Wbishopeval = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

Wrookeval = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
]

Queeneval = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

Wkingeval= [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
    [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
]

#=======================================Black eval

Bpawneval = Wpawneval[::-1]
Bbishopeval = Wbishopeval[::-1]
Brookeval = Wrookeval[::-1]
Bkingeval = Wkingeval[::-1]

# print(Brookeval)

boardmarkings ={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8
}

deathscoring= {'p': 10,
          'n': 30,
          'b': 30,
          'r': 50,
          'q': 90,
          'k': 100,
          'P': -10,
          'N': -30,
          'B': -30,
          'R': -50,
          'Q': -90,
          'K': -100,
        'None': 0,
        None:0
          }
def getvalueof_piece(piece, x, y):
    if piece == "P":
        return -10 + Wpawneval[y][x]
    elif piece == "p":
        return 10 + Bpawneval[y][x]
    elif piece == "N":
        return -30 + knighteval[y][x]
    elif piece == "n":
        return 30 + knighteval[y][x]
    elif piece == "B":
        return -30 + Wbishopeval[y][x]
    elif piece == "b":
        return 30 + Bbishopeval[y][x]
    elif piece == "R":
        return -50 + Wrookeval[y][x]
    elif piece == "r":
        return 50 + Brookeval[y][x]
    elif piece == "Q":
        return -90 + Queeneval[y][x]
    elif piece == "q":
        return 90 + Queeneval[y][x]
    elif piece == "K":
        return -100 + Wkingeval[y][x]
    elif piece == "k":
        return +100 + Bkingeval[y][x]

def fen_to_board(fen):
    board = {}
    ranks = fen.split(' ')[0].split('/')

    for i, rank in enumerate(ranks):
        file_num = 1
        for char in rank:
            if char.isnumeric():
                file_num += int(char)
            else:
                piece = char
                board.setdefault(piece, []).append(f"{chr(ord('a') + file_num - 1)}{8 - i}")
                file_num += 1

    return board

def evalboard(BOARD):
    score = 0;
    piecesandpositions = fen_to_board(BOARD.fen())

    for everykey in piecesandpositions:
        for everyposition in piecesandpositions[everykey]:
            # print(boardmarkings[everyposition[0]],everyposition[-1], everykey)
            score += getvalueof_piece(everykey, boardmarkings[everyposition[0]]-1, int(everyposition[-1])-1)

    return score

def mostvalueagent(BOARD):
    moves = list(BOARD.legal_moves)
    scores = []

    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)

        scores.append(evalboard(temp))

        if BOARD.turn == True:
            best_move = moves[scores.index(min(scores))]
        else:
            best_move = moves[scores.index(max(scores))]

    return best_move


def MinMaxN(Board, N):
    moves = list(Board.legal_moves)
    scores = []

    for move in moves:
        # now we make black move to check the future
        temp = deepcopy(Board)
        temp.push(move)
        scoreofdeath = 0

        if N>1:
            temp_bestmove = MinMaxN(temp, N-1)
            if temp_bestmove is None:
                scores.append(0)
                continue
            temp.push(temp_bestmove)

        scores.append(evalboard(temp))

    if Board.turn == True:
        if moves is None:
            return
        best_move = moves[scores.index(max(scores))]
    else:
        print(moves, scores)
        if len(moves) == 0 and len(scores) == 0:
            return
        best_move = moves[scores.index(max(scores))]

    return best_move




def MinMax(board):
    return MinMaxN(board, 3)
