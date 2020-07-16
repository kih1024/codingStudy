import sys
from collections import deque


def bfs(S, water):
    dq = deque()
    for r, c in water:
        dq.append([r, c, 0, "W"])
    r, c = S
    dq.append([r, c, 0, "S"])

    while dq:
        r, c, depth, kind = dq.popleft()
        if (r, c) == D and kind == "S":
            return depth
        if kind == "S":
            if (r, c) not in visited and (r, c) not in visitedW:
                visited[(r, c)] = True
                for i in range(4):
                    y = r + dy[i]
                    x = c + dx[i]
                    if y >= R or y < 0 or x >= C or x < 0:
                        continue
                    if arr[y][x] == "." and (y, x) not in visited:
                        dq.append([y, x, depth + 1, "S"])
                    if arr[y][x] == "D":
                        dq.append([y, x, depth + 1, "S"])
        else:
            if (r, c) not in visitedW:
                visitedW[(r, c)] = True
                for i in range(4):
                    y = r + dy[i]
                    x = c + dx[i]
                    if y >= R or y < 0 or x >= C or x < 0:
                        continue
                    if (arr[y][x] == "." or arr[y][x] == "S") and (
                        y,
                        x,
                    ) not in visitedW:
                        arr[y][x] = "*"
                        dq.append([y, x, depth + 1, "W"])

    return "KAKTUS"


R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for i in range(R)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited, visitedW = dict(), dict()
water = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == "*":
            water.append((i, j))
        elif arr[i][j] == "D":
            D = (i, j)
        elif arr[i][j] == "S":
            S = (i, j)

print(bfs(S, water))
