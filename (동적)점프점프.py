from collections import deque

N = int(input())
arr = list(map(int, map(int, input().split())))

dp = [1e9] * 1200
dp[0] = 0

for i in range(N):
    now = arr[i]

    for k in range(1,now+1):
        dp[i + k] = min(dp[i + k], dp[i] + 1)

if dp[N - 1] == 1e9:
    print(-1)
else:
    print(dp[N - 1])
