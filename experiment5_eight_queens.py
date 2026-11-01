
# Experiment 5: 8-Queens Problem Using Backtracking

N = 8
board = [-1] * N
placement_attempts = 0

def is_safe(row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        # Check same column
        if previous_col == col:
            return False

        # Check diagonals
        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve_queens(row):
    global placement_attempts

    # All eight queens have been placed
    if row == N:
        return True

    for col in range(N):
        placement_attempts += 1

        if is_safe(row, col):
            board[row] = col

            if solve_queens(row + 1):
                return True

            # Backtrack if the placement fails
            board[row] = -1

    return False


print("--- 8-QUEENS RESULT ---")

if solve_queens(0):
    print("Valid chessboard arrangement:\n")

    for row in range(N):
        print(" ".join(
            "Q" if board[row] == col else "."
            for col in range(N)
        ))

    print("\nPositions of all queens (row, column):")

    for row, col in enumerate(board):
        print(f"Queen {row + 1}: ({row + 1}, {col + 1})")

    print("\nPlacement attempts:", placement_attempts)
else:
    print("No solution exists.")
