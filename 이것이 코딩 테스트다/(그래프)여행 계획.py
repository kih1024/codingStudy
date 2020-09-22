#  서로서 집합 알고리즘

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
parent = [0] * N
for i in range(N):
    parent[i] = i

for i in range(len(plan)):
    plan[i] -= 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            union(parent, i, j)

travel = True
for i in range(M - 1):
    if parent[plan[i]] != parent[plan[i + 1]]:
        travel = False
        break
if travel:
    print("YES")
else:
    print("NO")

print(parent)


# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
