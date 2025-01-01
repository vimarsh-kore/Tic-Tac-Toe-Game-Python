import os

# Function to display the game board
def display_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        row = " | ".join(board[i * 3:(i + 1) * 3])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")

# Function to check for a winner
def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            return board[condition[0]]
    return None

# Function to save the game state
def save_game_state(board, current_player):
    with open(FILE_NAME, "w") as file:
        for i in range(3):
            file.write(",".join(board[i * 3:(i + 1) * 3]) + "\n")
        file.write(f"Player Turn: {current_player}\n")
    print("Game state saved!")

# Function to load the game state
def load_game_state():
    if not os.path.exists(FILE_NAME):
        print("No saved game found. Starting a new game.")
        return ["-"] * 9, 1

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        board = [cell for line in lines[:3] for cell in line.strip().split(",")]
        current_player = int(lines[3].strip().split(": ")[1])
    print("Game state loaded!")
    return board, current_player

# Function to check if the board is full (draw)
def is_draw(board):
    return "-" not in board

# Main game function
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")

    # Load or initialize the game
    board, current_player = load_game_state()

    while True:
        display_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"Player {1 if winner == 'X' else 2} ({winner}) wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        print(f"Player {current_player}, it's your turn.")
        move = input("Enter your move (1-9) or 's' to save and quit: ")

        if move.lower() == 's':
            save_game_state(board, current_player)
            break

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        move = int(move) - 1
        if board[move] != "-":
            print("That spot is already taken. Choose another.")
            continue

        board[move] = "X" if current_player == 1 else "O"
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    tic_tac_toe()

