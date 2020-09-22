N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in (j - 1, j + 1):
            if 0 <= k < 10:
                dp[i][j] += dp[i - 1][k]

print(sum(dp[N]) % 1000000000)