from collections import deque


def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = True
    count = 1
    while dq:
        y, x = dq.popleft()

        for i, v in enumerate([1, 2, 4, 8]):
            # 빈 공간 탐색
            if arr[y][x] & v != 0:
                continue
            ny, nx = y + dy[i], x + dx[i]

            if ny >= m or ny < 0 or nx >= n or nx < 0:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                count += 1
                dq.append((ny, nx))

    return count


dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]
visited = [[False] * n for _ in range(m)]
one, two, three = 0, 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            one += 1
            area = bfs(i, j)
            two = max(two, area)
print(one)
print(two)
for i in range(m):
    for j in range(n):
        li = [4, 8]
        if i == m - 1:
            del li[1]
        if j == n - 1:
            del li[0]
        for v in li:
            visited = [[False] * n for _ in range(m)]
            if arr[i][j] & v == 0:
                continue
            arr[i][j] -= v
            area = bfs(i, j)
            arr[i][j] += v
            three = max(three, area)
print(three)

