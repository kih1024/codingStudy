# https://www.acmicpc.net/problem/14002
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
rev = [i for i in range(n)]
idx = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                rev[i] = j
    if dp[idx] < dp[i]:
        idx = i

print(dp[idx])
result = []
while idx != rev[idx]:
    result.append(arr[idx])
    idx = rev[idx]
result.append(arr[idx])
result.reverse()
for i in result:
    print(i, end=" ")
