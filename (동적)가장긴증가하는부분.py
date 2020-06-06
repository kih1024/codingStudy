# https://www.acmicpc.net/problem/11053
n = int(input())

# dp[i] i번째 수를 마지막 원소로 가지는 lis의 최대길이
dp = [1] * n
li = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(max(dp))
