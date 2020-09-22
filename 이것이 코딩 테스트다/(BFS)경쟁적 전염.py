import sys
from collections import deque

input = sys.stdin.readline

def BFS(birus):
    global N, S
    dq = deque(birus)

    while dq:
        b, y, x, c = dq.popleft()

        if c == S:
            return

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if visited[ny][nx] == 0:
                visited[ny][nx] = b
                dq.append((b, ny, nx, c + 1))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
N, K = map(int, input().split())
visited = [list(map(int, input().split())) for _ in range(N)]
S, Y, X = map(int, input().split())
Y, X = Y - 1, X - 1
birus = []
for i in range(N):
    for j in range(N):
        if visited[i][j] != 0:
            birus.append((visited[i][j], i, j, 0))

birus.sort()
BFS(birus)
print(visited[Y][X])

