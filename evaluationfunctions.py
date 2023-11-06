from copy import deepcopy
scoring= {'p': 1,
          'n': 3,
          'b': 3,
          'r': 5,
          'q': 9,
          'k': 0,
          'P': -1,
          'N': -3,
          'B': -3,
          'R': -5,
          'Q': -9,
          'K': 0,
          }
def eval_board(BOARD):
    score = 0
    pieces = BOARD.piece_map()
    for key in pieces:
        score += scoring[str(pieces[key])]

    return score

def most_value_agent(BOARD, forcolor):

    moves = list(BOARD.legal_moves)
    scores = []
    for move in moves:
        #creates a copy of BOARD so we dont
        #change the original class
        temp = deepcopy(BOARD)
        temp.push(move)

        scores.append(eval_board(temp))

        if forcolor == "white":
            best_move = moves[scores.index(min(scores))]
        else:
            best_move = moves[scores.index(max(scores))]
    return best_move



def MinMax(BOARD):
    moves = list(BOARD.legal_moves)
    scores = []

    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)
        #black move ended

        forwhitemove = most_value_agent(temp, "white")
        # white move ended
        temp.push(forwhitemove)

        fornextbackmove = most_value_agent(temp, "black")
        # next black move ended
        temp.push(fornextbackmove)

        fornextwhitemove = most_value_agent(temp, "white")
        # level 4 never fold
        temp.push(fornextwhitemove)

        forlastblackmove = most_value_agent(temp, "Black")
        # level 4 never fold
        temp.push(forlastblackmove)

        scores.append(eval_board(temp))

    bestmove = moves[scores.index(max(scores))]

    return bestmove

