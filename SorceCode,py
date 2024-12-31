import os

def display_board(board):
    print("Current Board:")
    for row in board:
        print(" | ".join(row))
        print("---+---+---")

def initialize_board():
    return [["-", "-", "-"] for _ in range(3)]

def save_game_state(board, player_turn):
    with open("game_state.txt", "w") as file:
        for row in board:
            file.write(",".join(row) + "\n")
        file.write(f"Player Turn: {player_turn}\n")
    print("Game state saved!")

def load_game_state():
    if not os.path.exists("game_state.txt"):
        print("No saved game found. Starting a new game.")
        return initialize_board(), 1

    with open("game_state.txt", "r") as file:
        lines = file.readlines()
        board = [line.strip().split(",") for line in lines[:3]]
        player_turn = int(lines[3].split(": ")[1])
        return board, player_turn

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != "-" for row in board for cell in row)

def make_move(board, move, player_symbol):
    row, col = divmod(move - 1, 3)
    if board[row][col] == "-":
        board[row][col] = player_symbol
        return True
    else:
        print("Invalid move. Cell already occupied.")
        return False

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O\n")

    board, player_turn = load_game_state()
    symbols = ["X", "O"]

    while True:
        display_board(board)
        if is_full(board):
            print("The game is a draw!")
            break

        winner = check_winner(board)
        if winner:
            print(f"Player {symbols.index(winner) + 1} ({winner}) wins!")
            break

        print(f"Player {player_turn}, enter your move (1-9): ", end="")
        try:
            move = int(input().strip())
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue

            if make_move(board, move, symbols[player_turn - 1]):
                save_game_state(board, player_turn)
                player_turn = 3 - player_turn
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    play_game()
