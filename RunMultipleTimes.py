import chess

from ChessBotMethods import *
import matplotlib.pyplot as plt
import chess
def run_multiple_games(num_games):
    total_moves_list = []
    wins_white = 0
    wins_black = 0

    for i in range(num_games):
        board = chess.Board()
        print(f"\nGame {i + 1} --------------------------")
        board.reset()  # Reset the board for each game

        # Decide which color the player will control randomly
        winner, total_moves = main(board, False, i+1) # black is minmax and white is stockfish or human

        if board.outcome():
            total_moves_list.append(total_moves)
            if  winner == chess.WHITE:
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
    plt.show()
    directory_path = 'screenshots of 50 games/'
    file_name = f'overall50game.png'
    file_path = directory_path + file_name
    plt.savefig(file_path)

if __name__ == "__main__":
    num_games_to_play = 50
    run_multiple_games(num_games_to_play)