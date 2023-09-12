cost = {0: 0}

def AStarSearch(adj_matrix, heuristic, goal):
    closed = []
    # open = [current node, f(n), parent]
    open = [[0, heuristic[0], '']]

    while True:
        print(open)
        fn = [i[1] for i in open]
        # choosing min f(n) value from open list
        chosen_index = fn.index(min(fn))
        # current node
        node = open[chosen_index][0]
        # removing node from open and putting it in closed
        closed.append(open[chosen_index])
        del open[chosen_index]

        # if goal state is reached
        if closed[-1][0] == goal:
            break

        for i in range(len(adj_matrix[node])):
            if adj_matrix[node][i] != 0:
                # if node is already visited
                if i in [closed_item[0] for closed_item in closed]:
                    continue
                # update open list
                else:
                    cost.update({i:cost[node]+adj_matrix[node][i]})
                    fn_node = cost[node] + adj_matrix[node][i] + heuristic[i]
                    temp = [i, fn_node, node]
                    open.append(temp)

    # finding optimal path
    optimal_path = []

    item = goal
    while item!=0:
        print("item = ", item)
        for x in closed:
            if x[0]==item:
                optimal_path.append(x[0])
                item = x[2]
                break
    optimal_path.append(0)

    optimal_path.reverse()
    return closed, optimal_path

n = int(input("Enter no. of vertices: "))
adj_mat = [0]*n;

print("Enter Adjacency Matrix(The distance b/w nodes)")
for i in range(n):
    adj_mat[i] = [int(x) for x in input().split(" ")]

print("Enter heuristic values of each node: ", end='')
heuristic = [int(x) for x in input().split(" ")]

goal = int(input("Enter goal state: "))

visited_nodes, path = AStarSearch(adj_mat, heuristic, goal)
print('visited nodes: ' + str(visited_nodes))
print('path: ' + str(path))