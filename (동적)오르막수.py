N = int(input())
dp = [[0] * 11 for i in range(N + 1)]
# dp[i][j] = i자리 수이고 끝자리가 j 일때, 나올 수 있는 오르막수의 갯수
for j in range(1, 11):
    dp[1][j] = 1
for i in range(2, N + 1):
    for j in range(1, 11):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(sum(dp[N]) % 10007)
