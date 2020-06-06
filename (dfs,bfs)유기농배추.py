# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(100000)

def dfs(nowY, nowX):
    visited[nowY][nowX] = True
    for i in range(4):
        tempY = nowY + y[i]
        tempX = nowX + x[i]

        if 0 <= tempY <= n - 1 and 0 <= tempX <= m - 1:
            if arr[tempY][tempX] == 1 and visited[tempY][tempX] == False:
                dfs(tempY, tempX)


testcase = int(input())
x = [0, 1, 0, -1]
y = [-1, 0, 1, 0]
for _ in range(testcase):
    count = 0
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for i in range(k):
        first, second = map(int, input().split())
        arr[second][first] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                count += 1
                dfs(i, j)
    print(count)

