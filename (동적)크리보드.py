N = int(input())
dp = [0 for i in range(101)]
dp[1], dp[2], dp[3] = 1, 2, 3

count = 0
temp = 1
for i in range(4, 101):
    count += 1
    if count == 3:
        dp[i] = dp[i - 3] * 2
        temp = dp[i - 3]
        count = 0
        print(i, temp)
    else:
        dp[i] = dp[i - 1] + temp

    if i == N:
        break
print(dp)
# print(dp[N])
