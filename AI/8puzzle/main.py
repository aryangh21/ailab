from queue import PriorityQueue

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def calculate_heuristic(state):
    # Calculate the number of misplaced tiles
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced

def generate_successors(state):
    successors = []
    row, col = find_empty_tile(state)

    # Move the empty tile to the left
    if col > 0:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
        successors.append(new_state)

    # Move the empty tile to the right
    if col < 2:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]
        successors.append(new_state)

    # Move the empty tile up
    if row > 0:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
        successors.append(new_state)

    # Move the empty tile down
    if row < 2:
        new_state = [row[:] for row in state]
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]
        successors.append(new_state)

    return successors

def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def solve_8_puzzle(initial_state):
    explored = set()
    parent_map = {}

    # Initialize the priority queue
    queue = PriorityQueue()
    queue.put((calculate_heuristic(initial_state), initial_state))
    parent_map[tuple(map(tuple, initial_state))] = None

    while not queue.empty():
        _, current_state = queue.get()

        if current_state == goal_state:
            # Found the goal state
            break

        explored.add(tuple(map(tuple, current_state)))

        # Generate successor states
        successors = generate_successors(current_state)
        for successor in successors:
            if tuple(map(tuple, successor)) not in explored:
                queue.put((calculate_heuristic(successor), successor))
                parent_map[tuple(map(tuple, successor))] = current_state

    # Retrieve the solution path
    solution_path = []
    current = current_state
    while current is not None:
        solution_path.append(current)
        current = parent_map[tuple(map(tuple, current))]
    solution_path.reverse()

    return solution_path

# Test the function
# initial_state = [[1, 2, 3], [4, 6, 8], [7, 5, 0]]
print("Enter initial state - ")
initial_state = []
for i in range(3):
    row = [int(x) for x in input().split(' ')]
    initial_state.append(row)

solution_path = solve_8_puzzle(initial_state)

if solution_path:
    print("Solution Path:")
    for state in solution_path:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
