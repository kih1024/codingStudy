n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
items = []

for i in range(1, n+1):
    nowW, nowV = map(int, input().split())
    for j in range(k + 1):
        if j < nowW:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nowW] + nowV)

print(dp[n][k])

