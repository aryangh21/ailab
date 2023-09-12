from collections import defaultdict

graph = defaultdict(list)
tree = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)

def dfs(graph, n):
    visited = [False]*n
    stack = []
    ans = []

    stack.append(0);
    visited[0] = True;

    while(len(stack)!=0):
        front = stack.pop();
        ans.append(front)

        for x in graph[front]:
            if visited[x]==False:
                stack.append(x)
                visited[x] = True;

    return ans

def bfs_tree(tree, root):
    visited = {}
    stack = []
    ans = []

    stack.append(root);
    visited[root] = True;

    while (len(stack) != 0):
        front = stack.pop();
        ans.append(front)

        arr = tree[front]
        for x in arr:
            if x not in visited:
                stack.append(x)
                visited[x] = True;

    return ans



n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

for i in range(e):
    print("Enter edge ", i)
    u = int(input("Enter u: "))
    v = int(input("Enter v: "))
    add_edge(graph, u, v)
    add_edge(graph, v, u)

print(graph)

ans = dfs(graph, n)
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


