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

Bpawneval =  [row[::-1] for row in reversed(Wpawneval)]
Bbishopeval =   [row[::-1] for row in reversed(Wbishopeval)]
Brookeval =   [row[::-1] for row in reversed(Wrookeval)]
Bkingeval =   [row[::-1] for row in reversed(Wkingeval)]

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
          }




def getvalueof_piece(piece, x, y):
    if piece == "P":
        return 10 + Wpawneval[y][x]
    elif piece == "p":
        return -10 + Bpawneval[y][x]
    elif piece == "N":
        return 30 + knighteval[y][x]
    elif piece == "n":
        return -30 + knighteval[y][x]
    elif piece == "B":
        return 30 + Wbishopeval[y][x]
    elif piece == "b":
        return -30 + Bbishopeval[y][x]
    elif piece == "R":
        return 50 + Wrookeval[y][x]
    elif piece == "r":
        return -50 + Brookeval[y][x]
    elif piece == "Q":
        return 90 + Queeneval[y][x]
    elif piece == "q":
        return -90 + Queeneval[y][x]
    elif piece == "K":
        return 100 + Wkingeval[y][x]
    elif piece == "k":
        return -100 + Bkingeval[y][x]


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

def evalboard_colorbased(BOARD, side):
    score = 0
    pieces_and_positions = fen_to_board(BOARD.fen())

    for piece, positions in pieces_and_positions.items():
        if side == 'white' and piece.isupper():
            for position in positions:
                value = getvalueof_piece(piece, boardmarkings[position[0]] - 1, int(position[-1]) - 1)
                # print(f"Piece: {piece}, Position: {position}, Value: {value}")
                score += value
        elif side == 'black' and piece.islower():
            for position in positions:
                value = getvalueof_piece(piece, boardmarkings[position[0]] - 1, int(position[-1]) - 1)
                # print(f"Piece: {piece}, Position: {position}, Value: {value}")
                score += value

    return score

def evalboard(BOARD):
    score = 0;
    piecesandpositions = fen_to_board(BOARD.fen())

    for everykey in piecesandpositions:
        for everyposition in piecesandpositions[everykey]:
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


def MinMaxroot(Board, N, ismaximizingplayer):
    moves = list(Board.legal_moves)
    best_movescore = float("-inf")
    best_move_found = None

    for move in moves:
        Board.push(move)
        value = MinMax(Board, N-1, float('-inf'), float('inf'), not ismaximizingplayer)
        Board.pop()

        if value >= best_movescore:
            best_movescore = value
            best_move_found = move

    return best_move_found

def MinMax(Board, N, alpha, beta, ismaximizingplayer):
    if N == 0 or Board.is_game_over():
        return -evalboard(Board)

    moves = list(Board.legal_moves)

    if not ismaximizingplayer:
        best_movescore = float("-inf")

        for move in moves:
            Board.push(move)
            best_movescore = max(best_movescore, MinMax(Board, N-1, alpha, beta, not ismaximizingplayer))
            Board.pop()

            alpha = max(alpha, best_movescore)

            if beta <= alpha:
                return best_movescore

        return best_movescore

    else:
        best_movescore = float("inf")

        for move in moves:
            Board.push(move)
            best_movescore = min(best_movescore, MinMax(Board, N - 1, alpha, beta, not ismaximizingplayer))
            Board.pop()

            beta = min(beta, best_movescore)

            if beta <= alpha:
                return best_movescore

        return best_movescore
