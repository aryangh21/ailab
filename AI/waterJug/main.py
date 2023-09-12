from collections import deque, defaultdict

def print_path(path, front):
    if front[0]==0 and front[1]==0:
        print(0, " ", 0)
        return
    print_path(path, path[front])
    print(front[0], " ", front[1])


def water_jug_bfs(a, b, target):
    visited = {}
    path = {}
    isSolvable = False

    queue = deque(())
    queue.append((0, 0))

    while len(queue)!=0:
        front = queue.popleft()
        if front in visited:
            continue

        if front[0]>a or front[1]>b or front[0]<0 or front[1]<0:
            continue

        visited[front] = True

        if front[0]==target or front[1]==target:
            isSolvable = True
            print(path)
            print_path(path, front)
            # print final state
            if front[0]==target:
                if front[1]!=0:
                    print(front[0], " ", 0)
            else:
                if(front[0]!=0):
                    print(0, " ", front[1])
            return

        # completely fill jug 2
        if (front[0], b) not in visited:
            queue.append((front[0], b))
            path[(front[0], b)] = front
        # completely fill jug 1
        if (a, front[1]) not in visited :
            queue.append((a, front[1]))
            path[(a, front[1])] = front

        # jug 1 -> jug 2
        d = b - front[1]
        if front[0]>=d:
            c = front[0] - d
            if (c, b) not in visited :
                queue.append((c, b))
                path[(c, b)] = front
        else:
            c = front[0]+front[1]
            if (0, c) not in visited:
                queue.append((0, c))
                path[(0, c)] = front

        # jug 2 -> jug 1
        d = a - front[0]
        if front[1] >= d:
            c = front[1] - d
            if (0, c) not in visited:
                queue.append((a, c))
                path[(a, c)] = front
        else:
            c = front[0] + front[1]
            if (c, 0) not in visited:
                queue.append((c, 0))
                path[(c, 0)] = front

        # empty jug 2
        if (front[0], 0) not in visited:
            queue.append((front[0], 0))
            path[(front[0], 0)] = front
        # empty jug 1
        if (0, front[1]) not in visited:
            queue.append((0, front[1]))
            path[(0, front[1])] = front

    if isSolvable==False:
        print("No Solution!")







jug1 = int(input("Enter capacity of jug 1: "))
jug2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target value to be measured: "))
print("Steps Followed - ")
water_jug_bfs(jug1, jug2, target)

# intergchange dictionary key and values target can be multiple
# find number of values for particular key and create