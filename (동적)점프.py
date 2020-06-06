N = int(input())
miro = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][1] = 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        t = miro[i - 1][j - 1]
        if dp[i][j] == 0 or t == 0:
            continue
        if i + t < N + 1:
            dp[i + t][j] += dp[i][j]
        if j + t < N + 1:
            dp[i][j + t] += dp[i][j]

for i in dp:
    print(i)
print(dp[N][N])
