# https://rebas.kr/770

from collections import deque
from sys import stdin

input = stdin.readline


def bfs(r, c):
    global h, w
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    dq = deque()
    visited[r][c] = 0
    dq.append((r, c))
    while dq:
        r, c = dq.popleft()

        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y < 0 or y >= h + 2 or x < 0 or x >= w + 2:
                continue
            if visited[y][x] >= 0 or arr[y][x] == "*":
                continue
            if arr[y][x] == ".":
                visited[y][x] = visited[r][c]
                dq.appendleft((y, x))
            elif arr[y][x] == "#":
                visited[y][x] = visited[r][c] + 1
                dq.append((y, x))
    return visited


dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
for _ in range(int(input())):
    h, w = map(int, input().split())
    arr = ["." * (w + 2)]
    for i in range(h):
        arr.append(list("." + input().strip() + "."))

    arr.append(list("." * (w + 2)))
    q = deque()
    for i in range(h + 2):
        for j in range(w + 2):
            if arr[i][j] == "$":
                arr[i][j] = "."
                q.append((i, j))

    r, c = q.pop()
    b1 = bfs(r, c)
    r, c = q.pop()
    b2 = bfs(r, c)
    b3 = bfs(0, 0)
    ans = 1e9
    for i in range(h + 2):
        for j in range(w + 2):
            if arr[i][j] == "*":
                continue
            s = b1[i][j] + b2[i][j] + b3[i][j]
            if arr[i][j] == "#":
                s -= 2
            ans = min(ans, s)
    print(ans)
