import sys

# dp[i][j] : (i,j) 위치가 종착점일때, 가장 오래 살아 남을 수 있는 일수
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dp = [[1] * n for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 1
s = []
for i in range(n):
    for j in range(n):
        s.append((arr[i][j], i, j))

s.sort()
for v, r, c in s:
    temp = []
    for k in range(4):
        y, x = r + dy[k], c + dx[k]
        if y >= n or y < 0 or x >= n or x < 0:
            continue
        if v > arr[y][x]:
            temp.append(dp[y][x])

    if len(temp) > 0:
        dp[r][c] = max(temp) + 1

    answer = max(answer, dp[r][c])

print(answer)
