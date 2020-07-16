# import sys

# n, k = map(int, sys.stdin.readline().split())
# dp = [1e9] * 100001
# dp[0] = 0
# for i in range(n):
#     t = int(sys.stdin.readline())
#     dp[t] = 1

# for i in range(1, k + 1):
#     for j in range(1, (i // 2) + 1):
#         if dp[j] == 1e9 or dp[i - j] == 1e9:
#             continue
#         dp[i] = min((dp[j] + dp[i - j]), dp[i])

# if dp[k] == 1e9:
#     print(-1)
# else:
#     print(dp[k])


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
d = [-1] * (k + 1)
d[0] = 0

for x in coin:
    for y in range(1, k + 1):
        if y - x >= 0 and d[y - x] != -1:
            if d[y] == -1:
                d[y] = d[y - x] + 1
            else:
                d[y] = min(d[y], d[y - x] + 1)

print(d[k])
