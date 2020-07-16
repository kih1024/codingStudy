# https://www.acmicpc.net/problem/1525

from collections import deque


def bfs(m):
    visited[m] = 0
    dq = deque([m])

    while dq:
        now = dq.popleft()
        if now == 123456789:
            return visited[now]

        s = str(now)

        idx = s.find("9")
        r, c = idx // 3, idx % 3
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            y, x = r + dy, c + dx
            if y >= 3 or y < 0 or x >= 3 or x < 0:
                continue
            n_idx = y*3 + x
            ns = list(s)
            ns[idx],ns[n_idx] = ns[n_idx],ns[idx]
            i_ns = int("".join(ns))
            if i_ns not in visited:
                visited[i_ns] = visited[now] + 1
                dq.append(i_ns)
    return -1



arr = [list(map(int, input().split())) for _ in range(3)]
visited = dict()
m = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            arr[i][j] = 9
        m = m * 10 + arr[i][j]

print(bfs(m))



# from collections import deque

# def bfs():
#     while q:
#         d = q.popleft()
#         if d == 123456789:
#             print(dist[d])
#             return
#         s = str(d)
#         k = s.find('9')
#         x, y = k//3, k%3
#         for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
#             nx, ny = x+dx, y+dy
#             if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
#                 continue
#             nk = nx*3 + ny
#             ns = list(s)
#             ns[k], ns[nk] = ns[nk], ns[k]
#             nd = int(''.join(ns))
#             if not dist.get(nd):
#                 dist[nd] = dist[d]+1
#                 q.append(nd)
#     print(-1)

# q = deque()
# dist = dict()
# a = [list(map(int, input().split())) for _ in range(3)]
# m = 0
# for i in range(3):
#     for j in range(3):
#         n = a[i][j]
#         if not n:
#             n = 9
#         m = m*10 + n
# q.append(m)
# print(m)
# dist[m] = 0
# bfs()
