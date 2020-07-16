# https://www.acmicpc.net/problem/3055, 이 '탈출' 문제랑 푸는 방식 비슷함
# https://www.acmicpc.net/problem/5427
from collections import deque


def bfs():
    global w, h
    dq = deque(fire)
    while dq:
        r, c = dq.popleft()

        for i in range(4):
            y, x = r + dy[i], c + dx[i]

            if y >= h or y < 0 or x >= w or x < 0:
                continue
            if arr[y][x] != "#" and d_f[y][x] == -1:
                d_f[y][x] = d_f[r][c] + 1
                dq.append((y, x))

    dq.append(s)
    d_p[s[0]][s[1]] = 0

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            y, x = r + dy[i], c + dx[i]

            if y >= h or y < 0 or x >= w or x < 0:
                return d_p[r][c] + 1
            if d_p[y][x] == -1 and arr[y][x] not in "*#":
                if d_f[y][x] == -1 or d_p[r][c] + 1 < d_f[y][x]:
                    d_p[y][x] = d_p[r][c] + 1
                    dq.append((y, x))

    return "IMPOSSIBLE"


dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
testcase = int(input())

for _ in range(testcase):
    w, h = map(int, input().split())
    arr = [list(input()) for i in range(h)]
    d_f = [[-1] * w for _ in range(h)]
    d_p = [[-1] * w for _ in range(h)]
    fire = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "@":
                s = (i, j)
            elif arr[i][j] == "*":
                fire.append((i, j))
                d_f[i][j] = 0

    print(bfs())
