from copy import deepcopy

# Scoring values for each piece
scoring = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 100,
           'P': -1, 'N': -3, 'B': -3, 'R': -5, 'Q': -9, 'K': -100}


# Evaluate the score of a given board position
def eval_board(BOARD):
    score = 0
    pieces = BOARD.piece_map()

    for key in pieces:
        score += scoring[str(pieces[key])]

    return score


# Choose the move with the highest/lowest evaluated score depending on the player color
def most_value_agent(BOARD, forcolor):
    moves = list(BOARD.legal_moves)
    scores = []
    best_move = None

    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)
        scores.append(eval_board(temp))

        if forcolor == "white":
            best_move = moves[scores.index(min(scores))]
        else:
            best_move = moves[scores.index(max(scores))]

    return best_move


# Implementation of a basic Minimax algorithm with fixed depth
def MinMax_Check(BOARD):
    moves = list(BOARD.legal_moves)
    scores = []

    # Iteratively simulate a few moves ahead using the most_value_agent function
    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)

        for _ in range(5):  # Fixed depth, simulate 5 moves ahead
            forwhitemove = most_value_agent(temp, "white")
            if forwhitemove is None:
                continue
            temp.push(forwhitemove)

            fornextbackmove = most_value_agent(temp, "black")
            if fornextbackmove is None:
                continue
            temp.push(fornextbackmove)

        scores.append(eval_board(temp))

    # Choose the move with the highest score
    if len(scores) == 0 and len(moves) == 1:
        bestmove = moves[0]
    else:
        bestmove = moves[scores.index(max(scores))]

    return bestmove

# This implementation might not be optimal for evaluating positions
# and making moves. we did consider alternate way of implementation, please look at BetterEvaluationFunction.py
