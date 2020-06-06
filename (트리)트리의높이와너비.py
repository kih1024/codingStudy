class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
        self.parent = None


def inOrder(node, depth):
    global location
    if node.left != -1:
        inOrder(tree[node.left], depth + 1)
    li[depth].append(location)
    location += 1
    if node.right != -1:
        inOrder(tree[node.right], depth + 1)

n = int(input())
li = [[] for _ in range(n + 1)]
tree = {}
root = 1
location = 1
    
for _ in range(n):
    root, left, right = map(int, input().split())
    tree[root] = Node(root, left, right)

for i in range(n+1):
    if i in tree:
        if tree[i].left != -1:
            tree[tree[i].left].parent = tree[i].root
        if tree[i].right != -1:
            tree[tree[i].right].parent = tree[i].root

# for i in range(n+1):
#     if i in tree:
#         print(f"{tree[i].root}의 부모는:",tree[i].parent)

for i in range(n+1):
    if i in tree:
        if tree[i].parent is None:
            root = tree[i].root

for i in range(n+1):
    if i in tree:
        if tree[i].left != -1:
            tree[tree[i].left].parent = tree[i].root
        if tree[i].right != -1:
            tree[tree[i].right].parent = tree[i].root


inOrder(tree[root], 1)
maxN = 1
maxD = 1

for depth in range(len(li)):
    # print(depth, li[depth])
    if li[depth]:
        width = li[depth][-1] - li[depth][0] + 1
        if width > maxN:
            maxN = width
            maxD = depth

print(maxD, maxN)
