# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(now):
    visit[now] = True
    print(now, end=" ")
    for i in li[now]:
        if visit[i] == False:
            dfs(i)


def bfs(now):
    dq.append(now)
    while dq:
        print(dq)
        now = dq.popleft()
        if visit[now] == False:
            print(now)
            visit[now] = True
            for i in li[now]:
                if visit[i] == False:
                    dq.append(i)


n, m, v = map(int, input().split())
li = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
dq = deque()

for _ in range(m):
    first, second = map(int, input().split())
    li[first].append(second)
    li[second].append(first)

for i in range(n + 1):
    li[i].sort()

dfs(v)
print()
for i in range(n + 1):
    visit[i] = False

bfs(v)


# # https://www.acmicpc.net/problem/1260
# from collections import deque

# result = []

# def dfs(now):
#     result.append(now)
#     for i in range(len(li[now])):
#         if li[now][i] not in result:
#             dfs(li[now][i])

# def bfs(now):
#     dq.append(now)
#     while dq:
#         now = dq.popleft()
#         if now not in result:
#             result.append(now)
#             for i in range(len(li[now])):
#                 if li[now][i] not in result:
#                     dq.append(li[now][i])

# n, m, v = map(int, input().split())
# li = [[] for _ in range(n + 1)]
# dq = deque()

# for _ in range(m):
#     first, second = map(int, input().split())
#     li[first].append(second)
#     li[second].append(first)

# for i in range(1, n + 1):
#     li[i] = sorted(li[i])

# dfs(v)
# for i in result:
#     print(i, end=' ')
# print()
# result.clear()
# bfs(v)

# for i in result:
#     print(i, end=' ')
