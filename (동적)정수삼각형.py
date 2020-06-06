# https://www.acmicpc.net/problem/1932
n = int(input())
arr = [[0 for _ in range(n+1)] for i in range(n+1)]
dp = [[0 for _ in range(n+1)] for i in range(n+1)]

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    for j in range(1,i+1):
        arr[i][j] = tmp[j-1]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+ arr[i][j]

print(max(dp[n]))

# arr = [list(map(int, input().split())) for i in range(n)]
# dp = [[0] * n for i in range(n)]
# dp[0][0] = arr[0][0]
# for i in range(1, n):
#     for j in range(i + 1):
#         if j == 0:
#             dp[i][j] = dp[i - 1][0] + arr[i][0]
#         elif j == i:
#             dp[i][j] = dp[i - 1][j - 1] + arr[i][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j - 1],dp[i - 1][j]) + arr[i][j]

# print(max(dp[n - 1]))

