from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.visited = False


def insert(root, value):
    if root is None:
        root = Node(value)
        return root
    if value < root.data:
        root.leftChild = insert(root.leftChild, value)
    else:
        root.rightChild = insert(root.rightChild, value)
    return root


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.leftChild)
        preorder(root.rightChild)


def bfs(root):
    stack = []
    ans = []

    stack.append(root)
    root.visited = True

    while len(stack)!=0:
        front = stack.pop()
        ans.append(front.data)

        if front.rightChild and front.rightChild.visited==False:
            stack.append(front.rightChild)
            front.rightChild.visited = True
        if front.leftChild and front.leftChild.visited==False:
            stack.append(front.leftChild)
            front.leftChild.visited = True

    print(ans)


n = int(input("Enter number of nodes in BST: "))
x = int(input("Enter root: "))
root = Node(x)

for i in range(1, n):
    v = int(input("Enter vertex " + str(i + 1) + ": "))
    root = insert(root, v)

print("Preorder traversal: ", end=' ')
preorder(root)
print()
print("Breadth First Search: ", end=" ")
bfs(root)
