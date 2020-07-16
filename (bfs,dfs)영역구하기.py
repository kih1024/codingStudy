from collections import deque

def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = 1
    count = 1
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                continue

            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dq.append((ny, nx))
                count += 1
    return count

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
M, N, K = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(K)]
visited = [[0] * N for _ in range(M)]
first = 0
second = []

for k in s:
    lx, ly, rx, ry = k
    ly, ry = M - ly, M - ry

    for i in range(ry, ly):
        for j in range(lx, rx):
            visited[i][j] = 1

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            first += 1
            second.append(bfs(i, j))

print(first)
second.sort()
second = map(str,second)
print(" ".join(second))
