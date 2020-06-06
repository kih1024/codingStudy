# https://www.acmicpc.net/problem/1991


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left


def preOrder(node):
    print(node.value, end="")
    if node.left != ".":
        preOrder(li[node.left])
    if node.right != ".":
        preOrder(li[node.right])


def inOrder(node):
    if node.left != ".":
        inOrder(li[node.left])
    print(node.value, end="")
    if node.right != ".":
        inOrder(li[node.right])


def postOrder(node):
    if node.left != ".":
        postOrder(li[node.left])
    if node.right != ".":
        postOrder(li[node.right])
    print(node.value, end="")


n = int(input())

li = {}
for _ in range(n):
    root, left, right = input().split(" ")
    li[root] = Node(root, left, right)

preOrder(li["A"])
print()
inOrder(li["A"])
print()
postOrder(li["A"])
print()
