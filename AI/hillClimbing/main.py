# # SuccList = {'A': [['B', 3], ['C', 2]], 'B': [['D', 2], ['E', 3]], 'C': [['F', 2], ['G', 4]], 'D': [['H', 1], ['I', 99]],
# #             'F': [['J', 1]]
# #     , 'G': [['K', 99], ['L', 3]]}
# Start = 'A'
# End = 'F'
SuccList = {}

# Prompt the user for input until they enter an empty string
while True:
    node = input("Enter a node (or press Enter to finish): ")

    # If the user presses Enter without entering a node, break the loop
    if node == '':
        break

    successors = []

    # Prompt the user for successor nodes and their costs
    while True:
        successor = input("Enter a successor node (or press Enter to finish): ")

        # If the user presses Enter without entering a successor, break the loop
        if successor == '':
            break

        cost = int(input("Enter the cost for the successor: "))

        successors.append([successor, cost])

    # Add the node and its successors to the dictionary
    SuccList[node] = successors

Start = input("Enter source: ")
End = input("Enter destination: ")

Closed = list()
SUCCESS = True
FAILURE = False


def MOVEGEN(N):
    New_list = list()
    if N in SuccList.keys():
        New_list = SuccList[N]

    return New_list


def SORT(L):
    L.sort(key=lambda x: x[1])
    return L


def heu(Node):  # Node = ['B',2]--> [Node[0],Node[1]]
    return Node[1]


def APPEND(L1, L2):
    New_list = list(L1) + list(L2)
    return New_list


def Hill_Climbing(Start, End):
    global Closed
    N = Start
    CHILD = MOVEGEN(N)
    SORT(CHILD)
    N = [Start, 5]
    print("\nStart=", N)
    print("Sorted Child List=", CHILD)
    newNode = CHILD[0]
    CLOSED = [N]

    while (heu(newNode) <= heu(N)) and (len(CHILD) != 0):
        print("\n--------------------------")
        N = newNode
        print("N=", N)
        CLOSED = APPEND(CLOSED, [N])
        CHILD = MOVEGEN(N[0])
        SORT(CHILD)
        print("Sorted Child List=", CHILD)
        print("CLOSED=", CLOSED)
        if N[0] == End:
            exit()
        if len(CHILD)==0:
            print("No solution found!")
            exit()
        newNode = CHILD[0]

    print("No solution found!")


    Closed = CLOSED


# Driver Code
Hill_Climbing(Start, End)  # call search algorithm



