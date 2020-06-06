from collections import deque


def BFS(row, col, depth):
    dq = deque([[row, col, depth]])

    while dq:
        r, c, count = dq.popleft()
        if visited[r][c] == False:
            visited[r][c] = True
            if r == n - 1 and c == m - 1:
                return count
            for i in range(4):
                y = r + dy[i]
                x = c + dx[i]
                if y < 0 or y >= n or x < 0 or x >= m:
                    continue
                if arr[y][x] == '1' and visited[y][x] == False:
                    dq.append([y, x, count + 1])


n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
visited = [[False] * m for i in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer=BFS(0, 0, 1)
print(answer)

