'''
IT IS A CHESS BOT MADE USING AI PROJECT
In this we will be working on a AI based chessbot which will initially made using AI concept called MIN-MAX.
on 03/11/2023
Task:

Make a GUI of chess board where a player can play the game
evalute the position on the board
MIN-MAX USAGE

pip install chess pygame
'''
import numpy as np
from evaluationfunctions import *
import chess.engine
from bettereval import *

#after installing required packages.
import pygame
import chess
import math
import matplotlib.pyplot as plt



# initialise dispay
x = 800
y = 800
import random

#color scheme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (0, 191, 255, 255)  # Light blue or cyan
ALTERNATE_COLOR_1 = (118, 150, 86)
ALTERNATE_COLOR_2 = (238, 238, 210)

pieces = {
    'P': pygame.image.load('chess-utils/w_pawn.png'),
    'N': pygame.image.load('chess-utils/w_horse.png'),
    'B': pygame.image.load('chess-utils/w_bishop.png'),
    'R': pygame.image.load('chess-utils/w_rook.png'),
    'Q': pygame.image.load('chess-utils/w_queen.png'),
    'K': pygame.image.load('chess-utils/w_king.png'),
    'p': pygame.image.load('chess-utils/b_pawn.png'),
    'n': pygame.image.load('chess-utils/b_horse.png'),
    'b': pygame.image.load('chess-utils/b_bishop.png'),
    'r': pygame.image.load('chess-utils/b_rook.png'),
    'q': pygame.image.load('chess-utils/b_queen.png'),
    'k': pygame.image.load('chess-utils/b_king.png'),
}

def analyze_moves(moves, gamenumber):
    board = chess.Board()
    scores = []
    i = 0
    for move in moves:
        board.push(move)
        if i % 2 == 0:
            scores.append(evalboard_colorbased(board, "white"))
        else:
            scores.append(abs(evalboard_colorbased(board, "black")))
        i = i+1

    print("Analysis completed.")
    # print("score of board basing on each move: ", scores)
    combined_moves = ["start", "start"] + [move.uci() for move in moves]
    combined_scores = [0, 0] + scores
    fig, ax = plt.subplots(figsize=(26,13))

    # Plot moves with alternating positive and negative scores
    plt.plot(combined_moves, combined_scores, marker='o', linestyle='-', color='black')

    for i, score in enumerate(combined_scores):
        if i%2 == 0:
            plt.scatter([combined_moves[i]], [combined_scores[i]], color='green', marker='o', s=500)
        else:
            plt.scatter([combined_moves[i]], [combined_scores[i]], color='red', marker='x', s=500)

    # Set labels and title
    plt.xlabel("Moves")
    plt.ylabel("Move-based Score")
    plt.title(f'Game {gamenumber}: stockfish vs MinMax')

    # Show the plot
    plt.show()

    directory_path = 'screenshots of 50 games/'
    file_name = f'Game{gamenumber}.jpg'
    file_path = directory_path + file_name
    plt.savefig(file_path)



def UpdateBoard(screen, board):
    for i in range(64):
        piece = board.piece_at(i)
        if piece == None:
            pass
        else:
            screen.blit(pieces[str(piece)], ((i % 8) * 100, 700 - (i // 8) * 100))

    for i in range(7):
        i = i + 1
        pygame.draw.line(screen,WHITE, (0, i * 100), (800, i * 100))
        pygame.draw.line(screen, WHITE, (i * 100, 0), (i * 100, 800))

    pygame.display.flip()

def stockfish(BOARD, engine):
    return engine.play(BOARD, chess.engine.Limit(time = 0.1)).move
def random_agent1(BOARD):
    return MinMaxroot(BOARD, 3, BOARD.turn)

def main(board, agent_color, gamenumber):
    screen = pygame.display.set_mode((x, y))
    pygame.init()
    # initialize chessboard
    engine = chess.engine.SimpleEngine.popen_uci(
        "C:\\Users\\anude\\Downloads\\stockfish-windows-x86-64-avx2\\stockfish\\stockfish-windows-x86-64-avx2.exe")

    analysis = engine.analysis(chess.Board(), chess.engine.Limit(depth=30))
    print("Analysis of stockfish", analysis)


    '''
    for bot vs human game
    '''
    # make background black
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
            else:
                pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))

    # name window
    pygame.display.set_caption('Chess')

    # variable to be used later
    index_moves = []

    status = True # white moves first
    while (status):
        # update screen
        UpdateBoard(screen, board)
        #bot work
        if board.turn == agent_color:
            board.push(random_agent1(board))
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
                    else:
                        pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))
        #human work
        else:
            board.push(stockfish(board, engine))
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
                    else:
                        pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))
            # for event in pygame.event.get():
            #
            #     # if event object type is QUIT
            #     # then quitting the pygame
            #     # and program both.
            #     if event.type == pygame.QUIT:
            #         status = False
            #
            #     # if mouse clicked
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         # remove previous highlights
            #         for i in range(8):
            #             for j in range(8):
            #                 if (i + j) % 2 == 0:
            #                     pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
            #                 else:
            #                     pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))
            #
            #         # get position of mouse
            #         pos = pygame.mouse.get_pos()
            #
            #         # find which square was clicked and index of it
            #         square = (math.floor(pos[0] / 100), math.floor(pos[1] / 100))
            #         index = (7 - square[1]) * 8 + (square[0])
            #         # pygame.display.flip()
            #         # if we are moving a piece
            #         if index in index_moves:
            #
            #             move = moves[index_moves.index(index)]
            #
            #             board.push(move)
            #
            #             # reset index and moves
            #             index = None
            #             index_moves = []
            #
            #
            #         # show possible moves
            #         else:
            #             # check the square that is clicked
            #             piece = board.piece_at(index)
            #             # if empty pass
            #             if piece == None:
            #
            #                 pass
            #             else:
            #
            #                 # figure out what moves this piece can make
            #                 all_moves = list(board.legal_moves)
            #                 moves = []
            #                 for m in all_moves:
            #                     if m.from_square == index:
            #                         moves.append(m)
            #
            #                         t = m.to_square
            #                         TX1 = 100 * (t % 8)  # Center X of the square
            #                         TY1 = 100 * (7 - t // 8)  # Center Y of the square
            #
            #                         # highlight squares it can move to
            #                         pygame.draw.rect(screen, BLACK, pygame.Rect(TX1, TY1, 100, 100), 50)
            #                 index_moves = [a.to_square for a in moves]

        # deactivates the pygame library
        if board.outcome() != None:
            print(board.outcome())
            status = False
            print(board)
            print("Number of legal moves:", len(board.move_stack))
            print("move stack: ", board.move_stack)
            analyze_moves(board.move_stack, gamenumber)
            return board.outcome().winner , len(board.move_stack)
    pygame.quit()
    engine.quit()

# main(board,False)