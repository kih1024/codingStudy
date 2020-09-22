import sys
from collections import deque

input = sys.stdin.readline


def BFS(x):
    global K
    ans = []
    dq = deque([(x, 0)])
    visited[x] = True

    while dq:
        now, dis = dq.popleft()

        if dis == K:
            ans.append(now)

        if dis > K:
            break

        for i in route[now]:
            if not visited[i]:
                dq.append((i, dis + 1))
                visited[i] = True

    return ans

N, M, K, X = map(int, input().split())
route = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    f, s = map(int, input().split())
    route[f].append(s)

ans = BFS(X)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for a in ans:
        print(a)