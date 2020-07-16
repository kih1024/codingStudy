# https://www.acmicpc.net/problem/1012
from collections import deque


def bfs(i):
    global count
    dq = deque([i])
    while dq:
        now = dq.popleft()
        row = now // m
        col = now % m
        if visit[row][col] == False:
            visit[row][col] = True
            for j in range(4):
                dy = row + y1[j]
                dx = col + x1[j]
                if dy < 0 or dy > n - 1 or dx < 0 or dx > m - 1:
                    continue
                if visit[dy][dx] == False and arr[dy][dx] == 1:
                    dq.append(m * dy + dx)
    count += 1


testcase = int(input())
y1 = [0, 1, 0, -1]
x1 = [1, 0, -1, 0]
for t in range(testcase):
    count = 0
    m, n, k = map(int, input().split())
    visit = [[False] * m for i in range(n)]
    arr = [[0] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(m * n):
        row = i // m
        col = i % m
        if arr[row][col] == 1 and visit[row][col] == False:
            bfs(i)

    print(count)


# import sys
# sys.setrecursionlimit(100000)

# def dfs(nowY, nowX):
#     visited[nowY][nowX] = True
#     for i in range(4):
#         tempY = nowY + y[i]
#         tempX = nowX + x[i]

#         if 0 <= tempY <= n - 1 and 0 <= tempX <= m - 1:
#             if arr[tempY][tempX] == 1 and visited[tempY][tempX] == False:
#                 dfs(tempY, tempX)


# testcase = int(input())
# x = [0, 1, 0, -1]
# y = [-1, 0, 1, 0]
# for _ in range(testcase):
#     count = 0
#     m, n, k = map(int, input().split())
#     arr = [[0] * m for _ in range(n)]
#     visited = [[False] * m for _ in range(n)]
#     for i in range(k):
#         first, second = map(int, input().split())
#         arr[second][first] = 1

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 1 and visited[i][j] == False:
#                 count += 1
#                 dfs(i, j)
#     print(count)

