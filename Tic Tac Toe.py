# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if the game is over
def is_game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True

    # Check if the board is full
    if ' ' not in board:
        return True

    return False

# Function to play the game
def play_game():
    player = 'X'
    while not is_game_over():
        print_board()
        move = input("Player " + player + ", enter your move (0-8): ")
        
        # Check if the move is valid
        if not move.isdigit() or int(move) < 0 or int(move) > 8 or board[int(move)] != ' ':
            print("Invalid move. Try again.")
            continue

        # Update the board with the move
        board[int(move)] = player

        # Switch players
        player = 'O' if player == 'X' else 'X'

    # Game over
    print_board()
    if ' ' not in board:
        print("It's a tie!")
    else:
        print("Player", player, "wins!")

# Start the game
play_game()