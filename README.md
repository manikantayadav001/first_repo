# Tic-Tac-Toe

This is a simple implementation of the Tic Tac Toe game in Python.


Game Description

Tic Tac Toe is a two-player game played on a 3x3 grid. The players take turns marking empty cells on the grid with their respective symbols, either 'X' or 'O'. The goal of the game is to be the first player to get three of their symbols in a row, either horizontally, vertically, or diagonally. If all cells are filled and no player has won, the game is a tie.


How to Play

Run the Python script tic_tac_toe.py.
The board will be displayed, showing the initial empty cells.
Player 'X' will be prompted to enter their move by specifying a number from 0 to 8, representing the cells on the board.
After entering a valid move, the board will be updated, and it will be player 'O's turn.
Players continue taking turns until there is a winner or a tie.
The game will end, and the final board state and result will be displayed.


Code Overview

The code consists of the following components:

board: A list representing the Tic Tac Toe board.

print_board(): A function to print the current state of the board.

is_game_over(): A function to check if the game is over.

play_game(): The main function that allows players to take turns and plays the game.


Game Logic

The play_game() function uses a while loop to continue the game until the is_game_over() function returns True. In each iteration, it displays the current board, prompts the current player for their move, validates the move, updates the board with the move, and switches the player for the next turn. Once the game is over, it displays the final board state and the result (tie or the winning player).


Requirements

Python 3.x
Running the Code
Ensure Python is installed on your system.
Save the code in a file named tic_tac_toe.py.
Open a terminal or command prompt.
Navigate to the directory where tic_tac_toe.py is saved.
Run the command python tic_tac_toe.py.


Contributing

Contributions to the code or suggestions for improvements are welcome. If you find any bugs or issues, please open an issue in the GitHub repository.


Acknowledgments

The implementation of this Tic Tac Toe game was inspired by various online tutorials and resources.
