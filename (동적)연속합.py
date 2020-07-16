# from collections import deque

# n = int(input())
# arr = list(map(int, input().split()))
# # dp = [0] * (n + 1)
# arr.sort(reverse=True)

# dq = deque(arr)
# print(dp)
# dp[1] = dq.popleft()
# for i in range(2, n):
#     temp = dq.popleft()
#     if dp[i - 1] >= dp[i - 1] + temp:
#         break
#     else:
#         dp[i] = dp[i - 1] + temp

# print(dp)

n = int(input())
origin = [0]
origin += list(map(int, input().split()))
# dp[i] : i번째 수까지 봤을때 나올 수 있는 가장 큰 합
dp = [0 for _ in range(n + 1)]
result = -1001

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1] + origin[i], origin[i])
    result = max(result, dp[i])
print(dp)
print(result)
