from collections import deque

def bfs(r, c):
    global answer, n
    dq = deque([(r, c)])
    while dq:
        rr, cc = dq.popleft()
        if not visited[rr][cc]:
            visited[rr][cc] = True
            for i in range(4):
                y = rr + dy[i]
                x = cc + dx[i]
                if y < 0 or y >= n or x < 0 or x >= n:
                    continue
                if not visited[y][x]:
                    dq.append((y, x))
    answer = max(answer, count)


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

maxV = 0
answer = 1
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
for a in arr:
    maxV = max(maxV, max(a))

for i in range(1, maxV):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] <= i:
                visited[r][c] = True
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                bfs(r, c)
                count += 1
    answer = max(answer, count)
print(answer)
