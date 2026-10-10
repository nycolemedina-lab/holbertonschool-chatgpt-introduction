def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)  # Adjusted length to span across "X | O | X"

def check_winner(board):
    # Rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_coordinate(prompt):
    """Safely gets a integer coordinate between 0 and 2."""
    while True:
        try:
            val = int(input(prompt))
            if val in (0, 1, 2):
                return val
            print("Invalid input! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a valid number (0, 1, or 2).")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"\nPlayer {player}'s turn:")
        
        row = get_valid_coordinate("Enter row (0, 1, or 2): ")
        col = get_valid_coordinate("Enter column (0, 1, or 2): ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        # Place the mark
        board[row][col] = player

        # 1. Check for win immediately after move
        if check_winner(board):
            print_board(board)
            print(f"\nCongratulations! Player {player} wins!")
            break

        # 2. Check for tie/draw
        if is_board_full(board):
            print_board(board)
            print("\nIt's a tie!")
            break

        # 3. Switch player only if game continues
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
