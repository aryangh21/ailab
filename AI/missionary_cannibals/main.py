# function to validate states
# check overflow and underflow
# check if missionary > cannibals
def is_valid(state):
    m1, c1, b, m2, c2 = state
    return 0<=m1<=3 and 0<=c1<=3 and 0<=m2<=3 and 0<=c2<=3 and (m1==0 or m1>=c1) and (m2==0 or m2>=c2)

def generate_next_states(state):
    m1, c1, b, m2, c2 = state
    # possible moves -
    # 1. move 1m 0c
    # 2. move 2m 0c
    # 3. move 0m 1c
    # 4. move 0m 2c
    # 5. move 1m 1c
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    next_states = []

    for dm, dc in moves:
        if b==1:
            # boat in on left side
            new_state = (m1 - dm, c1 - dc, 0, m2 + dm, c2 + dc)
        else:
            # boat in on right side
            new_state = (m1 + dm, c1 + dc, 1, m2 - dm, c2 - dc)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def dfs(start_state):
    stack = [(start_state, [start_state])]

    while len(stack)!=0:
        current_state, path = stack.pop()
        if current_state == (0, 0, 0, 3, 3):
            return path

        for next_state in generate_next_states(current_state):
            if next_state not in path:
                stack.append((next_state, path+[next_state]))
    return None



start_state = (3, 3, 1, 0, 0)
ans = dfs(start_state)
if ans:
    print("Solution paths - ")
    for state in ans:
        m1, c1, b, m2, c2 = state
        print(f"{m1} missionaries, {c1} cannibals, {'boat on left' if b==1 else 'boat on right'}, {m2} missionaries, {c2} cannibals")
else:
    print("No Solution")