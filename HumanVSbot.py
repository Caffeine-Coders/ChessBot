'''
============================================================== Human vs AI game work ===================================================================================
'''
import numpy as np
from EvaluationFunctions import *
import chess.engine
from BetterEvaluationFunction import *

# after installing required packages.
import pygame
import chess
import math
import matplotlib.pyplot as plt

# initialize display
x = 800
y = 800

# color scheme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (0, 191, 255, 255)  # Light blue or cyan
ALTERNATE_COLOR_1 = (118, 150, 86)
ALTERNATE_COLOR_2 = (238, 238, 210)

# Dictionary mapping piece symbols to corresponding image files
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
    # Initialize a chess board for analysis
    board = chess.Board()
    scores = []
    i = 0

    # Iterate through each move and evaluate the position after the move
    for move in moves:
        board.push(move)
        # Evaluate the position based on the player's color
        if i % 2 == 0:
            scores.append(evalboard_colorbased(board, "white"))
        else:
            scores.append(abs(evalboard_colorbased(board, "black")))
        i = i + 1

    print("Analysis completed.")

    # Create a plot to visualize the scores for each move
    combined_moves = ["start", "start"] + [move.uci() for move in moves]
    combined_scores = [0, 0] + scores

    # Set up the plot
    fig, ax = plt.subplots(figsize=(26, 13))

    # Plot moves with alternating positive and negative scores
    plt.plot(combined_moves, combined_scores, marker='o', linestyle='-', color='black')

    # Highlight positive scores in green and negative scores in red
    for i, score in enumerate(combined_scores):
        if i % 2 == 0:
            plt.scatter([combined_moves[i]], [combined_scores[i]], color='green', marker='o', s=500)
        else:
            plt.scatter([combined_moves[i]], [combined_scores[i]], color='red', marker='x', s=500)

    # Set labels and title
    plt.xlabel("Moves")
    plt.ylabel("Move-based Score")
    plt.title(f'Game {gamenumber}: stockfish vs MinMax')

    # Save the plot as an image
    plt.savefig(f'screenshots/game_{gamenumber}_plot.png')

    # Show the plot
    plt.show()


def UpdateBoard(screen, board):
    # Update the chessboard display based on the current board state

    # Iterate through each square on the chessboard
    for i in range(64):
        # Get the piece at the current square
        piece = board.piece_at(i)

        # If there is no piece at the square, do nothing
        if piece is None:
            pass
        else:
            # If there is a piece, blit (draw) the corresponding piece image on the screen
            # Commented out to disable drawing pieces for now
            screen.blit(pieces[str(piece)], ((i % 8) * 100, 700 - (i // 8) * 100))

    # Draw horizontal lines to separate the rows on the chessboard
    for i in range(7):
        i = i + 1
        pygame.draw.line(screen, WHITE, (0, i * 100), (800, i * 100))

    # Draw vertical lines to separate the columns on the chessboard
    for i in range(7):
        i = i + 1
        pygame.draw.line(screen, WHITE, (i * 100, 0), (i * 100, 800))

    # Update the display to show the changes
    pygame.display.flip()


def stockfish(BOARD, engine):
    # Function to get the move from the Stockfish engine
    # Commented out to disable using Stockfish for now
    return engine.play(BOARD, chess.engine.Limit(time=0.1)).move

def random_agent1(BOARD):
    # Function to get a move from the MinMax algorithm with fixed depth
    # Commented out to disable using MinMax for now
    return MinMaxroot(BOARD, 3, BOARD.turn)


def main(board, agent_color, gamenumber):
    # Initialize the pygame display and chess engine
    screen = pygame.display.set_mode((x, y))
    pygame.init()
    engine = chess.engine.SimpleEngine.popen_uci(
        "C:\\Users\\anude\\Downloads\\stockfish-windows-x86-64-avx2\\stockfish\\stockfish-windows-x86-64-avx2.exe")

    # Perform analysis on the initial chess position using Stockfish
    analysis = engine.analysis(chess.Board(), chess.engine.Limit(depth=30))
    print("Analysis of stockfish", analysis)

    # Set up the chessboard display
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
            else:
                pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))

    # Set the window caption
    pygame.display.set_caption('Chess')

    # Variables for later use
    index_moves = []

    # Game loop
    status = True  # White moves first
    while status:
        # Update the screen
        UpdateBoard(screen, board)

        # ================================================== Bot's move =================================================
        if board.turn == agent_color:
            board.push(random_agent1(board))
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
                    else:
                        pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))
        # ================================= Human's move ========================================
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Remove previous highlights
                    for i in range(8):
                        for j in range(8):
                            if (i + j) % 2 == 0:
                                pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
                            else:
                                pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))

                    # Get position of mouse
                    pos = pygame.mouse.get_pos()

                    # Find which square was clicked and its index
                    square = (math.floor(pos[0] / 100), math.floor(pos[1] / 100))
                    index = (7 - square[1]) * 8 + (square[0])

                    # If we are moving a piece
                    if index in index_moves:
                        move = moves[index_moves.index(index)]
                        board.push(move)

                        # Reset index and moves
                        index = None
                        index_moves = []

                    # Show possible moves
                    else:
                        # Check the square that is clicked
                        piece = board.piece_at(index)

                        # If empty, pass
                        if piece is None:
                            pass
                        else:
                            # Figure out what moves this piece can make
                            all_moves = list(board.legal_moves)
                            moves = []
                            for m in all_moves:
                                if m.from_square == index:
                                    moves.append(m)

                                    t = m.to_square
                                    TX1 = 100 * (t % 8)  # Center X of the square
                                    TY1 = 100 * (7 - t // 8)  # Center Y of the square

                                    # Highlight squares it can move to
                                    pygame.draw.rect(screen, BLACK, pygame.Rect(TX1, TY1, 100, 100), 50)
                            index_moves = [a.to_square for a in moves]

        # Check if the game has ended
        if board.outcome() is not None:
            print(board.outcome())
            status = False
            print(board)
            print("Number of legal moves:", len(board.move_stack))
            print("Move stack: ", board.move_stack)

            # Analyze and plot moves
            analyze_moves(board.move_stack, gamenumber)
            return board.outcome().winner, len(board.move_stack)

    # Quit pygame and the chess engine
    pygame.quit()
    engine.quit()

# Example usage:
board = chess.Board()
main(board, False, 0)  # un Comment out this line, as it starts the human vs AI chess game
