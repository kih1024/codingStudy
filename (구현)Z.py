# https://www.acmicpc.net/problem/1074


# def solve(n, x, y):
#     global result
#     global count
#     if n == 2:
#         count += 1
#         if x == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x == X and y + 1 == Y:
#             print(result)
#             return
#         result += 1
#         if x + 1 == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x + 1 == X and y + 1 == Y:
#             print(result)
#             return
#         result += 1
#         return
#     solve(n / 2, x, y)
#     solve(n / 2, x, y + n / 2)
#     solve(n / 2, x + n / 2, y)
#     solve(n / 2, x + n / 2, y + n / 2)


# count = 0
# result = 0
# N, X, Y = map(int, input().split(" "))
# solve(2 ** N, 0, 0)
# print(count)

N, r, c = map(int, input().split())


def Z(sz, row, col):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if row < sz * (i + 1) and col < sz * (j + 1):
                return (i * 2 + j) * sz * sz + Z(sz, row - sz * i, col - sz * j)


print(Z(2 ** N, r, c))

