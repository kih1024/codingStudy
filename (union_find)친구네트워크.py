testcase = int(input())


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    root1 = find(x)
    root2 = find(y)

    if root1 != root2:
        parent[root2] = root1
        number[root1] += number[root2]


for _ in range(testcase):
    f = int(input())
    parent = dict()
    number = dict()

    for _ in range(f):
        p1, p2 = input().split(" ")

        if p1 not in parent:
            parent[p1] = p1
            number[p1] = 1
        if p2 not in parent:
            parent[p2] = p2
            number[p2] = 1
        union(p1, p2)
        print(number[find(p1)])


# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         parent[x] = find(parent[x])
#         return parent[x]


# def union(x, y):
#     root1 = find(x)
#     root2 = find(y)
#     parent[root2] = root1


# parent = []

# for i in range(0,5):
#     parent.append(i)

# union(1,4)
# union(2,4)

# for i in range(1, len(parent)):
#     print(find(i), end=' ')