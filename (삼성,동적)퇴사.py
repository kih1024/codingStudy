n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [0] * n

# dp[i] : i일에 시작한 상담이 마지막 상담일때 벌수 있는 금액의 최댓값
for i in range(n):
    if i + arr[i][0] <= n:
        dp[i] = arr[i][1]
        for j in range(i):
            if j + arr[j][0] - 1 < i:
                dp[i] = max(dp[i], dp[j] + arr[i][1])
print(dp)
print(max(dp))


# N = int(input())
# table =[list(map(int, input().split())) for _ in range(N)]
# max_ = 0

# def func(day, pay):
#     global max_
#     if day >= N:
#         if day == N:
#             tot = sum(pay)
#         else:
#             tot = sum(pay[:-1])

#         if tot > max_:
#             max_ = tot
#         return

#     # 해당 날짜에 상담 X
#     func(day+1, pay)

#     # 해당 날짜에 상담 O
#     nday, npay = day+table[day][0], pay+[table[day][1]]
#     func(nday, npay)

# func(0, [])
# print(max_)
