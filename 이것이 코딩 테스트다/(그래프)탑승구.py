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


G = int(input())
P = int(input())

parent = [0] * (G + 1)

for i in range(G + 1):
    parent[i] = i

maxV = 0
result = 0
for _ in range(P):
    x = int(input())

    data = find(parent, x)

    if data == 0:
        break

    union(parent, data, data - 1)
    result += 1

print(result)

