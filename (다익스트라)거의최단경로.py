# https://www.acmicpc.net/problem/5719
import heapq
import sys
from collections import deque

input = sys.stdin.readline


def dijkstra():
    distance[s] = 0
    # print(distance)
    queue = []
    heapq.heappush(queue, [0, s])

    while queue:
        current_dist, current_vert = heapq.heappop(queue)

        if distance[current_vert] < current_dist:
            continue

        for dest, weight in arr[current_vert]:
            now_dist = current_dist + weight
            if now_dist < distance[dest] and visit[current_vert][dest] == False:
                distance[dest] = now_dist
                heapq.heappush(queue, [now_dist, dest])


def bfs():
    q = deque()
    q.append(d)
    while q:
        now = q.popleft()
        if now == s:
            continue
        for pre, cost in reverse[now]:
            if distance[now] == distance[pre] + cost:
                visit[pre][now] = True
                q.append(pre)


while True:
    n, m = map(int, input().split())
    arr = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())

    for _ in range(m):
        first, second, w = map(int, input().split())
        arr[first].append((second, w))
        reverse[second].append((first, w))
    # print(visit)
    distance = [1e9] * n
    dijkstra()
    bfs()
    distance = [1e9] * n
    dijkstra()
    if distance[d] != 1e9:
        print(distance[d])
    else:
        print(-1)
