# https://www.acmicpc.net/problem/1774
import math
import sys

input = sys.stdin.readline
def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def get_distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    c = math.sqrt((x * x) + (y * y))
    return c


edges = []
parent = {}
rank = {}
vert = []
n, m = map(int, input().split())

for _ in range(n):
    f, s = map(int, input().split())
    vert.append((f, s))

length = len(vert)
for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((get_distance(vert[i], vert[j]), i + 1, j + 1))

for node in range(1, n + 1):
    parent[node] = node
    rank[node] = 0

for i in range(m):
    f, s = map(int, input().split())
    union(f, s)

edges.sort()

count = 0
for edge in edges:
    w, v, u = edge
    if find(v) != find(u):
        union(v, u)
        count += w

print("%0.2f" % count)

# 입력으로 받은 간선들을 모든 간선에서 빼는 방식.
# n, m = map(int, input().split())
# vert = [(0, 0)] * (n + 1)
# already = [[] for _ in range(n + 1)]
# parent = [0] * (n + 1)
# rank = [0] * (n + 1)
# edges = []
# for i in range(1, n + 1):
#     f, s = map(int, input().split())
#     vert[i] = (f, s)
# # print(vert)
# for i in range(m):
#     f, s = map(int, input().split())
#     already[f].append(s)
#     already[s].append(f)
# # print(already)

# for node in range(1, n + 1):
#     parent[node] = node

# for i in range(1, len(already)):
#     for j in range(len(already[i])):
#         if find(i) != find(already[i][j]):
#             union(i, already[i][j])


# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j not in already[i]:
#             x = vert[i][0] - vert[j][0]
#             y = vert[i][1] - vert[j][1]
#             c = math.sqrt((x * x) + (y * y))
#             edges.append((c,i,j))

# edges.sort()
# count = 0
# for edge in edges:
#     w,v,u = edge
#     if find(v) != find(u):
#         union(v,u)
#         count += w

# # print(edges)
# # print(parent[4],rank[4])
# # print(parent[1],rank[1])
# # num = 2
# print("%0.2f" % count)
