from collections import deque

# dp[i][j] : i번째 수까지 계산 했을때 값이 j인 경우의 수
N = int(input())
arr = list(map(int, input().split()))
arr = deque(arr)
arr.appendleft(0)

dp = [[0] * 21 for i in range(101)]
dp[1][arr[1]] += 1

for i in range(2, N):
    for j in range(21):
        if dp[i - 1][j] != 0:
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[N - 1][arr[N]])

