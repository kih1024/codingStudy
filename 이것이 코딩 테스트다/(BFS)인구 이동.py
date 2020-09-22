import sys
from collections import deque

input = sys.stdin.readline

def BFS(r, c):
    global L, R, N
    temp = []
    dq = deque([(r, c)])
    visited[r][c] = True
    temp.append((r, c))
    sumV = arr[r][c]

    while dq:
        r, c = dq.popleft()
        for i in range(4):
            ny, nx = r + dy[i], c + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            v = abs(arr[ny][nx] - arr[r][c])
            if not visited[ny][nx] and L <= v <= R:
                visited[ny][nx] = True
                temp.append((ny, nx))
                sumV += arr[ny][nx]
                dq.append((ny, nx))

    if len(temp) == 1:
        return False

    avg = sumV // len(temp)
    for r, c in temp:
        arr[r][c] = avg

    return True


dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    visited = [[False] * N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i,j)
                idx += 1
    if idx == N*N:
        break
    ans += 1

print(ans)