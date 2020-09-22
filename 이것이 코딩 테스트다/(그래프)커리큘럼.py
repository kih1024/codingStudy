from collections import deque
from copy import deepcopy

# 위상정렬
N = int(input())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
times = [0] * (N + 1)

for i in range(1, N + 1):
    li = list(map(int, input().split()))
    times[i] = li[0]
    for j in li[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

result = deepcopy(times)
dq = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    now = dq.popleft()

    for v in graph[now]:
        result[v] = max(result[v], result[now] + times[v])
        indegree[v] -= 1

        if indegree[v] == 0:
            dq.append(v)

for i in range(1, N + 1):
    print(result[i])

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1