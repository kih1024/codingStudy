# https://www.acmicpc.net/problem/2606
from collections import deque


def bfs(s):
    global count
    dq = deque([s])
    while dq:
        now = dq.popleft()
        if visited[now] == False:
            visited[now] = True
            count += 1
            for i in arr[now]:
                if visited[i] == False:
                    dq.append(i)
    print(count - 1)


def dfs(s):
    global count
    count += 1
    visited[s] = True
    for i in arr[s]:
        if not visited[i]:
            dfs(i)


n = int(input())
s = int(input())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(s):
    first, second = map(int, input().split())
    arr[first].append(second)
    arr[second].append(first)

bfs(1)
# dfs(1)
print(count - 1)
