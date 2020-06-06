# https://www.acmicpc.net/problem/10282
import heapq


def dijkstra(start):
    distance = [1e9] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        current_distance, currnet_node = heapq.heappop(queue)

        if distance[currnet_node] < current_distance:
            continue

        for dest, weight in arr[currnet_node]:
            now_dist = current_distance + weight
            if now_dist < distance[dest]:
                distance[dest] = now_dist
                heapq.heappush(queue, [now_dist, dest])

    return distance


testcase = int(input())

for _ in range(testcase):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(d):
        f, s, t = map(int, input().split())
        arr[s].append((f, t))

    result = dijkstra(c)
    count = 0
    maxV = 0
    for i in range(len(result)):
        if result[i] != 1e9:
            count += 1
            maxV = max(maxV, result[i])

    print(count, maxV)

