from queue import PriorityQueue

n = int((input("Enter no. of vertices: ")))
e = int(input("Enter no. of edges: "))
graph = [[] for i in range(n)]

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def best_first_search(src, target):
    visited = [False] * n
    pq = PriorityQueue()
    # cost to source is 0
    pq.put((0, src))
    visited[src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))


for i in range(e):
    x, y, cost = input("Enter src, dest, cost: ").split()
    addedge(int(x), int(y), int(cost))

source = int(input("Enter source: "))
target = int(input("Enter target: "))

print("Path followed is: ", end=" ")
best_first_search(source, target)

print()
print(graph)

