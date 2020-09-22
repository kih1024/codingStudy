import sys

input = sys.stdin.readline

# 크루스칼 알고리즘
def find(parent, x):
    if x != parent[x]:
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
parent = [i for i in range(N + 1)]
edges = []
ans = 0
maxEdge = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += cost
        maxEdge = cost

print(ans - maxEdge)