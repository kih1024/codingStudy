# https://www.acmicpc.net/problem/2655
import sys
import copy

input = sys.stdin.readline

n = int(input())
arr = []
arr.append([0, 0, 0, 0])

for i in range(1, n + 1):
    s, h, w = map(int, input().split())
    arr.append([i, s, h, w])

arr = sorted(arr, key=lambda x: x[3])
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            # dp[i] = max(dp[i], dp[j] + arr[i][2])
            if dp[i] < dp[j] + arr[i][2]:
                dp[i] = dp[j] + arr[i][2]

max_value = max(dp)
result = []
for i in range(n, 0, -1):
    if dp[i] == max_value:
        result.append(arr[i][0])
        max_value = max_value - arr[i][2]

result.reverse()
print(len(result))
for i in result:
    print(i)
