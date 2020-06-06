import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [[[-2e9] * (M + 2) for _ in range(N + 1)] for _ in range(2)]
dp[0][1][0] = 0
for j in range(1, M + 1):
    dp[0][1][j] = arr[0][j - 1] + dp[0][1][j - 1]

for i in range(2, N + 1):
    for j in range(1, M + 1):
        dp[0][i][j] = max(
            dp[0][i - 1][j] + arr[i - 1][j - 1], dp[0][i][j - 1] + arr[i - 1][j - 1]
        )
    for j in range(M, 0, -1):
        dp[1][i][j] = max(
            dp[0][i - 1][j] + arr[i - 1][j - 1], dp[1][i][j + 1] + arr[i - 1][j - 1]
        )
        dp[0][i][j] = max(dp[0][i][j], dp[1][i][j])

print(dp[0][N][M])
