n, s, m = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)
dp = [[False] * (m + 1) for i in range(n + 1)]
dp[0][s] = True
# (n+1)(m+1) 의 dp 테이블을 만든다
for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i-1][j] == False:
            continue
        if j - arr[i-1] >= 0:
            dp[i][j-arr[i-1]] = True
        if j + arr[i-1] <= m:
            dp[i][j+arr[i-1]] = True
        # if j - arr[i - 1] >= 0:
        #     if dp[i - 1][j - arr[i - 1]] == True:
        #         dp[i][j] = True

        # if j + arr[i - 1] <= m:
        #     if dp[i - 1][j + arr[i - 1]] == True:
        #         dp[i][j] = True

print(dp)
result = -1
for j in range(m, -1, -1):
    if dp[-1][j] == True:
        result = j
        break

print(result)

