from collections import deque
from sys import stdin

input = stdin.readline

def bfs():
    global M, N, zero
    while dq:
        r, c, d = dq.popleft()
        if zero == 0:
            return d
        for i in range(4):
            y, x = r + dy[i], c + dx[i]

            if y < 0 or y >= N or x < 0 or x >= M:
                continue

            if not visited[y][x]:
                if arr[y][x] == 0:
                    dq.append((y, x, d + 1))
                    arr[y][x] = 1
                    zero -= 1
                visited[y][x] = True

        if zero == 0:
            return d + 1

    return False

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
visited = [[False] * M for _ in range(N)]
dq = deque([])
zero = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            dq.append((i, j, 0))
            visited[i][j] == True
        elif arr[i][j] == 0:
            zero += 1

if zero == 0:
    print(0)
else:
    result = bfs()
    if result == False:
        print(-1)
    else:
        print(result)
