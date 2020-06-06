# https://www.acmicpc.net/problem/1325
from collections import deque

# bfs 알고리즘은 큐에서 뺄때 카운트와 visit True 해도 되고 큐에 집어 넣을때 카운트와 visit True를 해도된다.
# 효율면에서는 후자가 더 나은것 같다

def bfs(i):
    dq = deque([i])
    count = 0
    while dq:
        temp = dq.popleft()
        if visited[temp] == False:
            visited[temp] = True
            count += 1
            for j in arr[temp]:
                if visited[j] == False:
                    dq.append(j)
    return count


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
result = []
maxN = -1
for i in range(m):
    first, second = map(int, input().split())
    arr[second].append(first)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    c = bfs(i)
    if c > maxN:
        result = [i]
        maxN = c
    elif c == maxN:
        result.append(i)
        maxN = c
for e in result:
    print(e, end=" ")

# for i in range(1, n + 1):
#     visited = [False] * (n + 1)
#     c = bfs(i)
#     result.append((i, c))
#     maxN = max(maxN, c)

# # print(result)
# for i in result:
#     if maxN == i[1]:
#         print(i[0], end=" ")

