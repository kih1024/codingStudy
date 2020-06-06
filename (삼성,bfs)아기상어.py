from collections import deque
import heapq

# bfs로 이용하되, 먹을수있는 것중에서 고르는것은 힙을 이용해야 한다.
# 즉, 더 위쪽이면서 그리고 더 왼쪽인 것을 먹어야 하며, 이것은 heapify을 통해서 정렬한다음 맨 앞에 것을 먹는다.
def bfs(pos, depth):
    global secs
    dq = deque([[pos, depth]])
    visited = [[False] * n for i in range(n)]
    li, pd = [], 0
    while dq:
        now = dq.popleft()
        sr, sc = now[0][0], now[0][1]
        d = now[1]
        if d != pd:
            if len(li) > 0:
                heapq.heapify(li)
                r, c = li[0][0], li[0][1]
                arr[r][c] = 0
                secs += d
                s[0], s[1] = r, c
                return True
            li = []
        pd = d
        if visited[sr][sc] == False:
            visited[sr][sc] = True
            for i in range(4):
                y = sr + dy[i]
                x = sc + dx[i]
                if y < 0 or y >= n or x < 0 or x >= n:
                    continue
                if visited[y][x] == False:
                    if arr[y][x] == 0 or arr[y][x] == size:
                        dq.append([[y, x], d + 1])
                    elif arr[y][x] < size:
                        dq.append([[y, x], d + 1])
                        li.append((y, x))
    return False


n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            s = [i, j]

size, secs, eat = 2, 0, 0
while True:
    result = bfs(s, 0)
    if result:
        eat += 1
        if size == eat:
            eat = 0
            size += 1
    else:
        break

print(secs)
