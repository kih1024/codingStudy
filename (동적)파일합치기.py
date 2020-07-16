# https://www.acmicpc.net/problem/11066
#  dp[i][j] : i에서 j까지 합하는데 필요한 최소 비용
#  dp[i][k] + d[k+1][j] + sum(arr[i] ~arr[j])
# 다이나믹에서 난이도 상 문제
testcase = int(input())

for _ in range(testcase):
    n, arr = int(input()), [0] + list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n + 1):
        s[i] = s[i - 1] + arr[i]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):  # 부분파일의 길이
        for j in range(1, n + 2 - i):  # 시작점
            dp[j][j + i - 1] = (
                min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)])
                + s[j + i - 1]
                - s[j - 1]
            )

    print(dp[1][n])

