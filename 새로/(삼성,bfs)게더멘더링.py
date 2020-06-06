import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def is_connect(a):
    if len(a) == 1:
        return True
    visited = [False] * 10
    dq = deque([a[0]])
    while dq:
        now = dq.popleft()
        if visited[now] == False:
            visited[now] = True
            for i in area[now][1]:
                if visited[i] == False and i in a:
                    dq.append(i)

    for i in a:
        if visited[i] == False:
            return False
    return True

def gather(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1

    if not is_connect(a1) or not is_connect(a2):
        return -1

    sum1, sum2 = 0, 0
    for i in a1:
        sum1 += area[i][0]
    for i in a2:
        sum2 += area[i][0]
    return abs(sum1 - sum2)

n = int(input())
area = [[0, []] for i in range(n)]
temp = list(map(int, input().split()))
for i in range(n):
    area[i][0] = temp[i]
    m = list(map(int, input().split()))
    for j in range(1, m[0] + 1):
        area[i][1].append(m[j] - 1)
temp = [i for i in range(n)]
answer = -1
for i in range(n // 2 + 1):
    for g1 in combinations(temp, i):
        g2 = []
        for j in range(n):
            if j not in g1:
                g2.append(j)

        result = gather(list(g1), g2)
        if answer == -1 or answer > result:
            if result != -1:
                answer = result

print(answer)
