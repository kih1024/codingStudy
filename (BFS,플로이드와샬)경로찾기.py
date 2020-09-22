from collections import deque
import sys

input = sys.stdin.readline

def BFS(r, c):
    visited = [False] * N
    dq = deque([r])

    while dq:
        s = dq.popleft()
        for e in route[s]:
            if not visited[e]:
                if e == c:
                    return True
                visited[e] = True
                dq.append(e)
    return False

N = int(input())
route = [[] for _ in range(N)]
ans = [[0] * N for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            route[i].append(j)

for i in range(N):
    for j in range(N):
        if BFS(i, j):
            ans[i][j] = 1

for i in ans:
    string = list(map(str, i))
    print(" ".join(string))

