# # mygraph = {
# #     'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
# #     'edges': [
# #         (7, 'A', 'B'),
# #         (5, 'A', 'D'),
# #         (7, 'B', 'A'),
# #         (8, 'B', 'C'),
# #         (9, 'B', 'D'),
# #         (7, 'B', 'E'),
# #         (8, 'C', 'B'),
# #         (5, 'C', 'E'),
# #         (5, 'D', 'A'),
# #         (9, 'D', 'B'),
# #         (7, 'D', 'E'),
# #         (6, 'D', 'F'),
# #         (7, 'E', 'B'),
# #         (5, 'E', 'C'),
# #         (7, 'E', 'D'),
# #         (8, 'E', 'F'),
# #         (9, 'E', 'G'),
# #         (6, 'F', 'D'),
# #         (8, 'F', 'E'),
# #         (11, 'F', 'G'),
# #         (9, 'G', 'E'),
# #         (11, 'G', 'F')
# #     ]
# # }

# # parent = dict()
# # rank = dict()


# # def find(node):
# #     # path compression 기법
# #     if parent[node] != node:
# #         parent[node] = find(parent[node])
# #     return parent[node]


# # def union(root1, root2):
# #     # root1 = find(node_v)
# #     # root2 = find(node_u)
    
# #     # union-by-rank 기법
# #     if rank[root1] > rank[root2]:
# #         parent[root2] = root1
# #     else:
# #         parent[root1] = root2
# #         if rank[root1] == rank[root2]:
# #             rank[root2] += 1
    
    
# # def make_set(node):
# #     parent[node] = node
# #     rank[node] = 0

# # def kruskal(graph):
# #     mst = list()
    
# #     # 1. 초기화
# #     for node in graph['vertices']:
# #         make_set(node)
    
# #     # 2. 간선 weight 기반 sorting
# #     edges = graph['edges']
# #     edges.sort()
    
# #     # 3. 간선 연결 (사이클 없는)
# #     for edge in edges:
# #         weight, node_v, node_u = edge
# #         v,u = find(node_v),find(node_u)
# #         if v != u:
# #             union(v, u)
# #             mst.append(edge)
    
# #     return mst

# # print(kruskal(mygraph))

# print(0^1)

# from itertools import combinations

# li = [1,3,9]
# print(list(combinations(li,2)))

# import time


# di = dict()
# for i in range(10000000):
#     di[i] = True
# st=time.time()
# if 9000000 in di:
#     print(time.time()-st)
# di2 = list()
# for i in range(10000000):
#     di2.append(i)
# st=time.time()
# if 9000000 in di2:
#     print(time.time()-st)

li = [1,2,3,4]

print(max(li))