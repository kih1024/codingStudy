from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

def dijkstra(s, e, distances):
    distances[s] = 0
    q = []
    heapq.heappush(q, [distances[s], s])

    while q:
        cur_dis, cur_node = heapq.heappop(q)

        if distances[cur_node] < cur_dis:
            continue

        for adjacent, weight in route[cur_node].items():
            distance = cur_dis + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, [distance, adjacent])

N, M, X = map(int, input().split())
route = defaultdict(dict)
ans = 0
for i in range(M):
    s, e, l = map(int, input().split())
    route[s][e] = l

# print(route)
# print(route[1][3])
distances1 = {node: 1e9 for node in route}
dijkstra(X, s, distances1)
# print(distances1)
for s in range(1, N + 1):
    distances2 = {node: 1e9 for node in route}
    dijkstra(s, X, distances2)
    # print(distances2)
    t = distances2[X] + distances1[s]
    ans = max(t, ans)

print(ans)

