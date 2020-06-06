# https://www.acmicpc.net/problem/1697
from collections import deque

def bfs():
    depth = 0
    q.append((s,depth))
    while q:
        now = q.popleft()
        first = now[0]
        second = now[1]
        if first == b:
            print(second)
            return
        if visit[first] == False:
            visit[first] = True
            li = [first * 2, first + 1, first - 1]
            second += 1
            for i in li:
                if i >= 0 and i <= 100000 and visit[i] == False:
                    q.append((i,second))


# def bfs_s():
#     q.append(s)
#     while q:
#         now_pos = q.popleft()
#         if now_pos == b:
#             print(arr[now_pos])
#             return
#         for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
#             if 0 <= next_pos < 100001 and arr[next_pos] == 0:
#                 arr[next_pos] = arr[now_pos] + 1
#                 q.append(next_pos)


s, b = map(int, input().split())
q = deque()
visit = [False] * 100001
arr = [0] * 100001
bfs()
# bfs_s()
