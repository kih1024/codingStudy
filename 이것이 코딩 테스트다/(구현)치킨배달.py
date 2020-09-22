from itertools import combinations

N, M = map(int, input().split())
arr = []
home, chiken = [], []
ans = 1e9
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            chiken.append((i, j))

for c in list(combinations(chiken, M)):
    d_dis = 0
    for h in home:
        c_min = 1e9
        for cc in c:
            dis = abs(h[0] - cc[0]) + abs(h[1] - cc[1])
            c_min = min(c_min, dis)
        d_dis += c_min
    ans = min(ans, d_dis)
print(ans)