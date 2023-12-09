import chess
from StockfishVSbot import *  # Assuming you have a module named StockfishVSbot with a function 'main'
import matplotlib.pyplot as plt

'''
This is the class which will run stockfish vs bot multiple times and analyze how many times did Stockfish win, how many times bot win and plots game numbers vs number of moves per game.
'''
def run_multiple_games(num_games):
    total_moves_list = []  # To store the total moves for each game
    wins_white = 0  # Counter for wins by White
    wins_black = 0  # Counter for wins by Black

    for i in range(num_games):
        board = chess.Board()
        print(f"\nGame {i + 1} --------------------------")
        board.reset()  # Reset the board for each game

        # Decide which color the player will control randomly
        winner, total_moves = main(board, False, i+1)  # Black is Minimax and White is Stockfish or human

        if board.outcome():
            total_moves_list.append(total_moves)
            if winner == chess.WHITE:
                wins_white += 1
            elif winner == chess.BLACK:
                wins_black += 1

    print("\n---------------------------------")
    print(f"Results after {num_games} games:")
    print(f"Wins for White: {wins_white}")
    print(f"Wins for Black: {wins_black}")
    print(f"Total moves for each game: {total_moves_list}")
    print(f"Average moves per game: {sum(total_moves_list) / num_games}")

    # Plotting
    plt.plot(range(1, num_games + 1), total_moves_list, marker='o')
    plt.xlabel("Game Number")
    plt.ylabel("Total Moves")
    plt.title(f"Total Moves in Each Game")
    plt.savefig("screenshots/numberof_moves_plot.png")  # Save the plot as an image
    plt.show()  # Display the plot

if __name__ == "__main__":
    num_games_to_play = 50
    run_multiple_games(num_games_to_play)
