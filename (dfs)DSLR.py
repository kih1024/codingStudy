from collections import deque
import sys

input = sys.stdin.readline


def process(now, o):
    if o == "D":
        t = (now * 2) % 10000
        return t
    elif o == "S":
        if now == 0:
            return 9999
        else:
            return now - 1
    elif o == "L":
        if now < 1000:
            now = now * 10
        else:
            nm = now // 1000
            na = now % 1000
            now = na * 10 + nm
        return now
    else:
        na = now % 10
        nm = now // 10
        now = na * 1000 + nm
        return now


def BFS():
    global A, B
    dq = deque([A])
    visited[A] = ""
    while dq:
        now = dq.popleft()
        if now == B:
            return visited[now]
        for o in op:
            nn = process(now, o)
            if nn not in visited:
                visited[nn] = visited[now] + o
                dq.append(nn)


op = ["D", "S", "L", "R"]
T = int(input())
for _ in range(T):
    visited = dict()
    A, B = input().split()
    A, B = int(A), int(B)
    print(BFS())