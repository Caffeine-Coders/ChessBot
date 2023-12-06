import random

import chess
import numpy as np
QTable = np.zeros((64,64))
learningRate = 0.1      #alpha
discountFactor = 0.9    #gamma
explorationRate = 0.1   #epsilon

def get_possible_moves(board):
    possible_moves =[]
    for move in board.legal_moves:
        possible_moves.append(move)

    return possible_moves

def select_move(board,QTable,explorationRate):
    if np.random.random() < explorationRate:
        return np.random.choice(get_possible_moves(board))
    else:
        best_move = None
        best_q_value = float('-inf')
        for move in get_possible_moves(board):
            q_val = QTable[move.from_square, move.to_square]
            if q_val > best_q_value:
                    best_q_value = q_val
                    best_move = move
        return best_move

def play_game(QTable,learningRate,discountFactor,explorationRate):
    board = chess.Board()
    while True:
        if board.turn == chess.BLACK:
            move = select_move(board,QTable,explorationRate)
        else:

            move = random.choice(list(board.legal_moves))
        board.push(move)

        if board.is_game_over():
            break
        reward = 0
        if board.is_checkmate():
            if board.turn == chess.BLACK:
                reward = -1
            else:
                reward = 1
        else:
            reward = 0

        current_q_val = QTable[move.from_square,move.to_square]
        new_q_val = reward + discountFactor * np.max(QTable[move.to_square,:])
        QTable[move.from_square,move.to_square] = (1-learningRate) * current_q_val + learningRate * new_q_val
for i in range(1000):
    play_game(QTable,learningRate,discountFactor,explorationRate)

np.save("QTable.npy",QTable)

