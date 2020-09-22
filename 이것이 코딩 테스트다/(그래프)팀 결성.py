# 크루스칼 알고리즘

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


# 같은 팀인지 체크
def ck(parent, a, b):
    if parent[a] != parent[b]:
        return False
    return True


N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    state, a, b = map(int, input().split())

    if state == 0:
        if not ck(parent, a, b):
            union(parent, a, b)
    else:
        if not ck(parent, a, b):
            print("NO")
        else:
            print("YES")