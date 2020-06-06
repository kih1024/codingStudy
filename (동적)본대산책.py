# https://www.acmicpc.net/problem/12849
#  dp[i][j] 는 i분 일때, j 위치에 있을 경우의 수
n = int(input())
route = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4, 5],
    [2, 3, 5, 6],
    [3, 4, 7],
    [4, 7],
    [5, 6],
]

dp = [[0] * 8 for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(8):
        temp = 0
        for k in route[j]:
            temp += dp[i - 1][k]
        dp[i][j] = temp % 1000000007

print(dp[n][0])
