# https://www.acmicpc.net/problem/1766

import heapq

# 선행적으로 해야 하는것을 고려하는것
# 위상정렬은 사이클이 없고(어떤게 먼저인지 모르기 때문) 방향성이 있어서 이 방향성을 거스리지 않는다.
# 즉, 노드를 정렬하되 선후 관계에 맞게 정렬한다.
# 시간 복잡도 O(V + E) , 노드의 갯수 + 간선의 갯수
n, m = map(int, input().split(" "))
li = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
heap = []
result = []

for _ in range(m):
    f, s = map(int, input().split(" "))
    li[f].append(s)
    indegree[s] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

# for _ in range(n):
while heap:
    minL = heapq.heappop(heap)
    result.append(minL)
    for i in li[minL]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end=" ")
