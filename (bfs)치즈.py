from collections import deque


def bfs(i, j):
    dq = deque([(i, j)])
    visited[i][j] = True
    isEdge = False
    temp = [(i,j)]
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if not isEdge:
                if ny == 0 or ny == n - 1 or nx == 0 or nx == m - 1:
                    isEdge = True

            if not visited[ny][nx] and arr[ny][nx] != 1:
                visited[ny][nx] = True
                dq.append((ny, nx))
                arr[ny][nx] = 0
                temp.append((ny, nx))

    if not isEdge:
        for r, c in temp:
            arr[r][c] = 2
    
def ck():
    some = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                return False
    return True


dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
time = 0

while True:
    time += 1
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] != 1:
                bfs(i, j)

    remove = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 1:
                continue
            count = 0
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if arr[ni][nj] == 0:
                    count += 1
            if count >= 2:
                remove.append((i,j))

    for r,c in remove:
        arr[r][c] = 0
    if ck():
        break

print(time)
