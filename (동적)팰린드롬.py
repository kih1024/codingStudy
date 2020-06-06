# import sys

# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# dp = [[0] * (N + 1) for _ in range(N + 1)]
# # print(li[0:4][::-1])
# for i in range(N):
#     if arr[:i+1] == arr[:i+1][::-1]:
#         dp[1][i+1] = 1

# dp[1][1]=0

# for i in range(2,N+1):
#     for j in range(N+1):
#         if dp[i-1][(j+1)%(N+1)] == 1:
#             dp[i][j] = 1

# for i in dp:
#     print(i)

# for t in range(M):
#     S,E = map(int,sys.stdin.readline().split())
#     if S == E:
#         print(1)
#         continue
#     print(dp[S][E])
import sys

n = int(input())
d = [int(i) for i in sys.stdin.readline().split()]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if d[i] == d[i+1]:
        dp[i][i+1] = 1
        
for l in range(2,n):
    for i in range(n-l):
        if d[i] == d[i+l] and dp[i+1][i+l-1] == 1:
            dp[i][i+l] = 1

m = int(input())

for _ in range(m):
    i,j = [int(a) for a in sys.stdin.readline().split()]
    print(dp[i-1][j-1])

for t in dp:
    print(t)