# Set up the game board as a list
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

# Define a function to print the game board
def print_game_board():
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])

# Define a function to handle a player's turn
def take_player_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")
    position = int(position) - 1
    while game_board[position] != "-":
        position = int(input("Position already taken. Choose a different position: ")) - 1
    game_board[position] = player
    print_game_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    if (game_board[0] == game_board[1] == game_board[2] != "-") or \
       (game_board[3] == game_board[4] == game_board[5] != "-") or \
       (game_board[6] == game_board[7] == game_board[8] != "-") or \
       (game_board[0] == game_board[3] == game_board[6] != "-") or \
       (game_board[1] == game_board[4] == game_board[7] != "-") or \
       (game_board[2] == game_board[5] == game_board[8] != "-") or \
       (game_board[0] == game_board[4] == game_board[8] != "-") or \
       (game_board[2] == game_board[4] == game_board[6] != "-"):
        return "win"
    # Check for a tie
    elif "-" not in game_board:
        return "tie"
    # Game is not over
    else:
        return "play"

# Define the main game loop
def play_tic_tac_toe():
    print_game_board()
    current_player = "X"
    game_over = False
    while not game_over:
        take_player_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_tic_tac_toe()
