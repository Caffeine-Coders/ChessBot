import random
import chess
import numpy as np
import math
import pygame
QTable = np.zeros((64,64))
# declaring the values of alpha, gamma and epsilon
learningRate = 0.1      #alpha
discountFactor = 0.9    #gamma
explorationRate = 0.1   #epsilon

# this method gets a list of all possible moves
def get_possible_moves(board):
    possible_moves =[]
    for move in board.legal_moves:
        possible_moves.append(move)

    return possible_moves

# this method based on the exploration rate selects whether to explor or exploit
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

# main training method of RL
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
    # number of iterations to be trained for
    play_game(QTable,learningRate,discountFactor,explorationRate)

np.save("QTable.npy",QTable)

#testing the RL method created
def RL_testing():
    Q = np.load("QTable.npy")
    # initialise dispay
    x = 800
    y = 800
    import random
    screen = pygame.display.set_mode((x, y))
    pygame.init()

    # color scheme
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    HIGHLIGHT_COLOR = (0, 191, 255, 255)  # Light blue or cyan
    ALTERNATE_COLOR_1 = (118, 150, 86)
    ALTERNATE_COLOR_2 = (238, 238, 210)

    # initialize chessboard
    board = chess.Board()

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

    def UpdateBoard(screen, board):
        for i in range(64):
            piece = board.piece_at(i)
            if piece == None:
                pass
            else:
                screen.blit(pieces[str(piece)], ((i % 8) * 100, 700 - (i // 8) * 100))

        for i in range(7):
            i = i + 1
            pygame.draw.line(screen, WHITE, (0, i * 100), (800, i * 100))
            pygame.draw.line(screen, WHITE, (i * 100, 0), (i * 100, 800))

        pygame.display.flip()

    def random_agent(BOARD):
        return select_move(BOARD, Q, 0)

    def main(board, agent_color):
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

        status = True  # white moves first
        while (status):
            # update screen
            UpdateBoard(screen, board)
            # bot work
            if board.turn == agent_color:
                board.push(random_agent(board))
                for i in range(8):
                    for j in range(8):
                        if (i + j) % 2 == 0:
                            pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
                        else:
                            pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))
            # human work
            else:
                for event in pygame.event.get():

                    # if event object type is QUIT
                    # then quitting the pygame
                    # and program both.
                    if event.type == pygame.QUIT:
                        status = False

                    # if mouse clicked
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # remove previous highlights
                        for i in range(8):
                            for j in range(8):
                                if (i + j) % 2 == 0:
                                    pygame.draw.rect(screen, ALTERNATE_COLOR_1, pygame.Rect(i * 100, j * 100, 100, 100))
                                else:
                                    pygame.draw.rect(screen, ALTERNATE_COLOR_2, pygame.Rect(i * 100, j * 100, 100, 100))

                        # get position of mouse
                        pos = pygame.mouse.get_pos()

                        # find which square was clicked and index of it
                        square = (math.floor(pos[0] / 100), math.floor(pos[1] / 100))
                        index = (7 - square[1]) * 8 + (square[0])
                        # pygame.display.flip()
                        # if we are moving a piece
                        if index in index_moves:

                            move = moves[index_moves.index(index)]

                            board.push(move)

                            # reset index and moves
                            index = None
                            index_moves = []


                        # show possible moves
                        else:
                            # check the square that is clicked
                            piece = board.piece_at(index)
                            # if empty pass
                            if piece == None:

                                pass
                            else:

                                # figure out what moves this piece can make
                                all_moves = list(board.legal_moves)
                                moves = []
                                for m in all_moves:
                                    if m.from_square == index:
                                        moves.append(m)

                                        t = m.to_square
                                        TX1 = 100 * (t % 8)  # Center X of the square
                                        TY1 = 100 * (7 - t // 8)  # Center Y of the square

                                        # highlight squares it can move to
                                        pygame.draw.rect(screen, BLACK, pygame.Rect(TX1, TY1, 100, 100), 50)
                                index_moves = [a.to_square for a in moves]

            # deactivates the pygame library
            if board.outcome() != None:
                print(board.outcome())
                status = False
                print(board)
        pygame.quit()

    main(board, False)

RL_testing()