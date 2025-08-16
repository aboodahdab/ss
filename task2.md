Assessment: Tic-Tac-Toe with AI Opponent
Objective

Build a complete Tic-Tac-Toe game in Python that:

Lets the player choose to play against another human or the computer.

Shows the board after every move.

Saves and loads the scoreboard from a file.

Uses functions to keep the code organized.

Requirements
Game Logic

3×3 grid board

Player 1 = "X", Player 2 (or computer) = "O"

Check for winner or draw

Replay option (play multiple games in one run)

Scoreboard

Keep track of wins, losses, draws

Save scoreboard to a file (tictactoe_scores.txt)

Load it at the start of the program

Functions

At least these functions:

print_board(board) → display the current board

check_winner(board) → check if X or O won

player_move(board) → ask user for move

computer_move(board) → simple AI (random free spot)

save_scores(scores) and load_scores() → file handling

Computer Opponent (AI)

Level 1: Pick a random available spot

Bonus Challenge: Block the player’s winning move if possible

Extra Challenges (Optional, for bonus points)

Make the computer try to win (not just block).

Add colored output (green for win, red for loss, yellow for draw).

Let the player choose grid size (3×3, 4×4, etc.).
