from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt

graph = defaultdict(list)
tree = defaultdict(list)
G = nx.Graph()


def add_edge(graph, u, v):
    graph[u].append(v)
    G.add_edge(u, v)


def bfs(graph, n):
    visited = [False] * n
    queue = deque([])
    ans = []

    queue.append(0);
    visited[0] = True;

    while (len(queue) != 0):
        front = queue.popleft();
        ans.append(front)

        for x in graph[front]:
            if visited[x] == False:
                queue.append(x)
                visited[x] = True;

    return ans

def bfs_tree(tree, root):
    visited = {}
    queue = deque([])
    ans = []

    queue.append(root);
    visited[root] = True;

    while (len(queue) != 0):
        front = queue.popleft();
        ans.append(front)

        arr = tree[front]
        for x in arr:
            if x not in visited:
                queue.append(x)
                visited[x] = True;

    return ans


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

for i in range(e):
    print("Enter edge ", i)
    u = int(input("Enter u: "))
    v = int(input("Enter v: "))
    add_edge(graph, u, v)
    # add_edge(graph, v, u)

print(graph)
nx.draw(G, with_labels=True)
plt.show()

ans = bfs(graph, n)
print(ans)

vertices = []
n = int(input("Enter number of vertices: "))
root = input("Enter root: ")
for i in input("Enter adjacency list: ").split():
    tree[root].append(i)
while True:
    x = input("Enter vertex: ")
    if x=='-1':
        break
    for i in input("Enter adjacency list: ").split():
        tree[x].append(i)
print(tree)

ans = bfs_tree(tree, root)
print(ans)
