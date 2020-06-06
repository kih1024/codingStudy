# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
chiken, home = [], []
answer = 1e9
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chiken.append((i, j))

select = list(combinations(chiken, m))

for k in select:
    total = 0
    for i in home:
        minV = 1e9
        for kk in k:
            minV = min(minV, abs(i[0] - kk[0]) + abs(i[1] - kk[1]))
        total += minV
    answer = min(answer, total)

print(answer)
