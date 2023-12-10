# Chess AI - Still Naive Bot

This project implements a simple chess AI using the Min-Max algorithm with evaluation functions. The game can be played in different modes, including human vs bot and bot vs bot.

## Prerequisites

Make sure you have Python installed on your system. Additionally, you'll need to install the following Python packages:

- [pygame](https://www.pygame.org/)
- [python-chess](https://python-chess.readthedocs.io/)
- [Stockfish](https://stockfishchess.org/)

## Installation

1. **Install Python:**

   Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

2. **Install pygame:**

   ```bash
   pip install pygame

3. **Install Python-Chess:**
   ```bash
   pip install python-chess
4. **Install StockFish:**
   ```bash
   https://stockfishchess.org/download/
   # we use windows OS and have installed the installed windows version of stockfish to use in Stockfish_FilePath.py

## How to Run
<b>Human vs bot:</b>
- initially navigate to HumanVSbot.py and uncomment the last two
lines of the code.
- if you are using it in IDE [pycharm], you can directly run the program and enjoy playing the game.
- if you want to run it through terminal
   ```bash
   python HumanVSbot.py

<b>Stockfish vs bot:</b>
- initially navigate to StockfishVSbot.py and uncomment the last two
lines of the code.
- also navigate to <b>Stockfish_FilePath.py</b> and update your stockfish excecutable file path.
- if you are using it in IDE [pycharm], you can directly run the program and enjoy watching the game between stockfish and MIN - MAX.
- if you want to run it through terminal
  ```bash
   python StockfishVSbot.py
## Limitations of RL making chess bot
<b>Alphago Zero:</b>
- To implement Alphago Zero, we are lacking the computational power. Because, this algorithm self plays from both the sides and learn from each move, It will take months to train the basic model to beat the level 3 minimax.

<b>Q learning with reward based on final game result and a random opponent:</b>
- What we did try was to implement a Q-Learning model for almost 50000 iterations, where in reward was presented basing on the result of the game.
- Opponent was a random agent, picking up random move out of all legal moves.
- Our bot still couldn't come up with a better strategy than MinMax.

<b>Q learning with reward function, and a specific opponent:</b>
- Multiple strategies were engaged to reward the bot, like capture based reward, and overall game based reward. 
- Here the opponent was engaged on a specific target, like Greedy choice, first legal move as choice and random choice.
   - Capture based reward: 
     - Game ends after 25 moves
     - Maximum captures, max reward. 
     - Uses Q Learning as technique.
   - Game based:
     - Plays general rule based chess and learns from it.
     - Uses Monte carlo search 
     - It was learning forever…….!


## Result
**Stockfish vs Bot game:**
- Move based score evaluation for both stockfish [green .] and bot [red X], please navigate to screenshots or TerminalLog_after50games.txt to view all game details.

<img src = "screenshots/game_0_plot.png"/>
 
      So as we see after certain point of the game we see a huge spike in 
      difference of score between players showing a bad move made by Min max bot.
       

- 50 concecute games later, graph of each game vs number of total moves per each game
   ```bash
   max number of moves = 81
   minimum number of moves = 21
   Average number of moves over 50 games = 38.92 
   
<img src = "screenshots/numberof_moves_plot.png"/>
## PPT explanation of project

- please checkout out ppt of the project at : https://tinyurl.com/535project

## Contributors
[![](https://github.com/anudeep-17.png?size=50)](https://github.com/anudeep-17)
[![](https://github.com/ForumShah8.png?size=50)](https://github.com/ForumShah8)
[![](https://github.com/DheerajNani7.png?size=50)](https://github.com/DheerajNani7)
