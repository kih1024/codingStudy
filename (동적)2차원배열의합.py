# https://www.acmicpc.net/problem/2167
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]
# dp[i][j] = 1,1 부터 i,j까지의 부분합
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, y, x = map(int, input().split())
    print(dp[y][x] - dp[i - 1][x] - dp[y][j - 1] + dp[i - 1][j - 1])

