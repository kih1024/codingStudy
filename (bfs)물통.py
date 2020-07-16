from collections import deque


def bfs(A, B, C):
    dq = deque([(0, 0, C)])
    volM = [A, B, C]
    visited[(0, 0, C)] = True

    while dq:
        now = dq.popleft()
        if now[0] == 0:
            answer.append(now[2])
        for i in range(6):
            new = [now[0], now[1], now[2]]
            pp, rr = p[i], r[i]
            if now[pp] == 0 or now[rr] == volM[rr]:
                continue
            minV = min(now[pp], volM[rr] - now[rr])
            new[pp] = now[pp] - minV
            new[rr] = now[rr] + minV
            new = tuple(new)

            if new not in visited:
                visited[new] = True
                dq.append(new)

p, r = [0, 0, 1, 1, 2, 2], [1, 2, 0, 2, 0, 1]

A, B, C = map(int, input().split())
visited = dict()
answer = []
bfs(A, B, C)
answer.sort()
for i in range(len(answer)):
    answer[i] = str(answer[i])
    
answer = " ".join(answer)
print(answer)

