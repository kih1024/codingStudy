import sys
# 런타임 오류 뜨면 써줌.
sys.setrecursionlimit(100000)

def dfs(r, c):
    minus = 0
    visited[r][c] = True
    for i in range(4):
        y = r + dy[i]
        x = c + dx[i]

        if y < 0 or y >= rr or x < 0 or x >= cc:
            continue

        if m[y][x] == 0:
            minus += 1

    for i in range(4):
        y = r + dy[i]
        x = c + dx[i]

        if y < 0 or y >= rr or x < 0 or x >= cc:
            continue
        if m[y][x] != 0 and visited[y][x] == False:
            dfs(y, x)
    m[r][c] = max(0, m[r][c] - minus)


rr, cc = map(int, input().split())
m = [list(map(int, input().split())) for i in range(rr)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

y = 0
while True:
    visited = [[False] * cc for i in range(rr)]
    count = 0
    temp = 0
    for i in m:
        temp += sum(i)
    if temp == 0:
        isFind = False
        break

    for r in range(rr):
        for c in range(cc):
            if m[r][c] == 0:
                visited[r][c] = True
                continue
            if not visited[r][c]:
                dfs(r, c)
                count += 1
    if count >= 2:
        result = y
        isFind = True
        break
    y+=1

if isFind:
    print(result)
else:
    print(0)
