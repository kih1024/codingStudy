# https://www.acmicpc.net/problem/9251
first = input()
second = input()
# 배열(표)를 행,렬 +1 만큼 크게 만드는 이유는 dp에서 그전의 행렬을 이용을 해야 하기 때문에
dp = [[0] * (len(first) + 1) for i in range(len(second) + 1)]
# dp에는 공통 subsequence의 최대길이가 들어감
for i in range(1, len(second) + 1):
    for j in range(1, len(first) + 1):
        if first[j - 1] == second[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


print(dp[-1][-1])
