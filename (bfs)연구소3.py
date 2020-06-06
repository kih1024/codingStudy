from itertools import combinations
from collections import deque


def bfs(pos, depth):
    global N, count
    dq = deque([])
    zero_count = 0
    for i in pos:
        dq.append((i, depth))

    while dq:
        p, d = dq.popleft()
        r, c = p // N, p % N
        if not visited[r][c]:
            visited[r][c] = True

            if arr[r][c] == 0:
                zero_count += 1

            if zero_count == count:
                return d

            for i in range(4):
                y = r + dy[i]
                x = c + dx[i]
                if y >= N or y < 0 or x >= N or x < 0:
                    continue
                if not visited[y][x] and arr[y][x] != 1:
                    dq.append((N * y + x, d + 1))

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
pos = []
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 1e9
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            pos.append(i * N + j)
        elif arr[i][j] == 0:
            count += 1

combi = list(combinations(pos, M))
for i in combi:
    visited = [[False] * N for i in range(N)]
    result = bfs(i, 0)
    if result != -1:
        answer = min(answer, result)

if answer == 1e9:
    print(-1)
else:
    print(answer)
