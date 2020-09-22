import sys
from collections import deque

input = sys.stdin.readline

for t in range(int(input())):
    ans = 0
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V + 1)

    for v in range(1, V + 1):
        if not visited[v]:
            # 아래부턴 BFS 코드
            dq = deque([v])
            visited[v] = 1

            while dq:
                idx = dq.popleft()

                for i in graph[idx]:
                    if visited[i] == 0:
                        visited[i] = visited[idx] * -1
                        dq.append(i)
                    elif visited[i] == visited[idx]:
                        ans = 1
                        break

    if ans == 1:
        print("NO")
    else:
        print("YES")
