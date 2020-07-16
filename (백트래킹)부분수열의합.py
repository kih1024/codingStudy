def dfs(some,pos):
    global ans,N,S
    if some == S:
        ans += 1
    if pos >= N:
        return

    for i in range(pos,N):
        some += arr[i]
        dfs(some,i+1)
        some -= arr[i]
   

N,S = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
dfs(0,0)
if S == 0:
    ans-=1
print(ans)
# N, S = map(int, input().split())

# arr = list(map(int, input().split()))


# def search(next=0, number_sum=0):
#     res = 0
#     if number_sum == S:
#         res = 1
#     if next >= N:
#         return res
#     for i in range(next, N):
#         res += search(i+1, number_sum + arr[i])
#     return res


# res = search()
# if S == 0:
#     res -= 1

# print(res)