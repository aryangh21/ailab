# using number of conflicts to the queen as heuristic function
from queue import PriorityQueue

def is_valid(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(n):
    board = [['*' for _ in range(n)] for _ in range(n)]
    solutions = []

    # Initialize the priority queue
    queue = PriorityQueue()
    # queue = (heuristic, row, board)
    queue.put((0, 0, board))

    while not queue.empty():
        _, row, current_board = queue.get()

        if row == n:
            # Found a valid solution
            solution = [''.join(row) for row in current_board]
            # print(solution)
            solutions.append(solution)
        else:
            for col in range(n):
                if is_valid(current_board, row, col, n):
                    # Place a queen at the current position
                    current_board[row][col] = 'Q'

                    # Calculate the priority based on the number of conflicts
                    priority = sum([1 for i in range(n) if not is_valid(current_board, i, col, n)])

                    # Add the new state to the priority queue
                    queue.put((priority, row + 1, [row[:] for row in current_board]))

                    # Remove the queen from the current position for backtracking
                    current_board[row][col] = '*'

    return solutions

# Test the function
n = int(input("Enter number of queens: "))
solutions = solve_n_queens(n)

# Print the solutions
print(f"Found {len(solutions)} solutions for {n}-Queens problem:")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
