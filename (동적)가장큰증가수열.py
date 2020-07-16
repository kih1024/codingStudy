# https://www.acmicpc.net/problem/11055
from copy import deepcopy

# dp[i]는 i까지왔을때 가장긴 부분수열의 합중에서 가장 큰 값
n = int(input())
arr = list(map(int, input().split()))
dp = deepcopy(arr)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + arr[i], dp[i])

print(max(dp))
