# Tic-Tac-Toe-Game-Python

# Tic Tac Toe Game

## Project Description
This is a console-based Tic Tac Toe game for two players, developed in Python. The game allows players to compete in a classic 3x3 grid format. Additionally, it features file handling to save and resume the game state, ensuring that players can pick up where they left off.

## Features Implemented
- **Interactive Console Interface**: Provides a user-friendly console-based interface for gameplay.
- **Two-Player Gameplay**: Supports two players, each taking turns to place their marks (X or O) on the board.
- **Game State Saving and Resuming**: Uses file handling to save the current board state and player turn to a file (game_state.txt).
- **Winner/Draw Detection**: Automatically detects when a player wins or when the game ends in a draw.
- **Error Handling**: Ensures invalid moves are handled gracefully.

## How to Run the Project

1. **Clone the Repository:**
2. 
   git clone <REPOSITORY_LINK>
   cd <REPOSITORY_FOLDER>

3. **Run the Script:**
   Make sure Python is installed on your system. Then execute the script:
   
   python tic_tac_toe_game.py

4. **Start Playing:**
   - Follow the on-screen instructions to start a new game or load a saved one.
   - Players take turns to input their moves (1-9), and the game displays the current state of the board after each move.

5. **Save Game State:**
   - The game automatically saves the state after every move into a file named game_state.txt.
   - You can resume the game later by rerunning the script.

6. **Exit:**
   - The game concludes when one player wins or if the game ends in a draw.

## File Handling Details
- The game_state.txt file saves the game board state and the player turn in the following format:
  
  X,O,X
  -,O,-
  X,-,-
  Player Turn: 2

## Future Improvements
- Add a single-player mode with AI.
- Enhance the interface with a GUI.
- Introduce difficulty levels for AI gameplay.

Feel free to contribute to the project or suggest enhancements!
