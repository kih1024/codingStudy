from collections import deque

def bfs(r, c):
    visited[r][c] = True
    dq = deque([(r, c, 0)])
    while dq:
        y, x, d = dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny >= N or ny < 0 or nx >= M or nx < 0:
                continue
            if not visited[ny][nx] and arr[ny][nx] == "L":
                visited[ny][nx] = True
                dq.append((ny, nx, d + 1))

    return d

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'W':
            continue
        visited = [[False] * M for i in range(N)]
        depth = bfs(i, j)
        ans = max(ans, depth)

print(ans)