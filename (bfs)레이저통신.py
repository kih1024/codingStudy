from collections import deque


def bfs():
    global H, W, dest
    result = 1e9

    while dq:
        y, x, d, c = dq.popleft()

        if y == dest[0] and x == dest[1]:
            result = min(result,c)

        for i in [0, 1, -1]:
            nd = (d + i) % 4
            if i != 0:
                nc = c + 1
            else:
                nc = c
            ny, nx = y + dy[nd], x + dx[nd]

            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue

            if visited[ny][nx] >= nc and arr[ny][nx] != "*":
                visited[ny][nx] = nc
                dq.append((ny, nx, nd, nc))

    return result

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
W, H = map(int, input().split())
arr = [list(input()) for _ in range(H)]
visited = [[912341234] * W for _ in range(H)]
dq = deque([])
C = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == "C":
            C.append((i, j))

start, dest = C[0], C[1]
visited[start[0]][start[1]] = 0
for i in range(4):
    sy, sx = start[0] + dy[i], start[1] + dx[i]

    if sy < 0 or sy >= H or sx < 0 or sx >= W:
        continue
    if arr[sy][sx] == "*":
        continue
    visited[sy][sx] = 0
    dq.append((sy, sx, i, 0))

ans = bfs()

print(ans)
