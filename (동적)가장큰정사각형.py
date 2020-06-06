# https://www.acmicpc.net/problem/1915
# dp[i][j] 는 i,j까지 왔을때, 가장 큰 정사각형의 한변의 길이
n, m = map(int, input().split())
arr = [[0] * (m + 1) for i in range(n + 1)]
dp = [[0] * (m + 1) for i in range(n + 1)]
maxV = 0
for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        arr[i + 1][idx + 1] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i][j] == 0:
            continue
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        maxV = max(dp[i][j], maxV)

print(maxV * maxV)
