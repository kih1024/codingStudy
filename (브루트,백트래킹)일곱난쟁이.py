def dfs(d, v, c):
    global isFind
    if c == 7:
        if v == 100:
            isFind = True
        return

    if d >= 9:
        return

    for i in range(2):
        if i == 0:
            visited[d] = True
            dfs(d + 1, v + h[d], c + 1)
        else:
            dfs(d + 1, v, c)

        if isFind:
            return
        visited[d] = False

h = []
ans = []
isFind = False
visited = [False] * 9
for _ in range(9):
    h.append(int(input()))

dfs(0, 0, 0)

for i in range(9):
    if visited[i]:
        ans.append(h[i])

ans.sort()
for a in ans:
    print(a)
