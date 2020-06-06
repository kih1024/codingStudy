# def recur(n, r, c):
#     if n==1:
#         if r==0 and c==0:
#             return 1
#         elif r==0 and c==1:
#             return 2
#         elif r==1 and c==0:
#             return 3
#         else:
#             return 4
#     if r > pow(2, n - 1)-1 and c > pow(2, n - 1)-1:
#         return 3 * pow(pow(2, n - 1),2) + recur(n - 1, r - pow(2, n - 1), c - pow(2, n - 1))
#     elif r > pow(2, n - 1)-1 and c <= pow(2, n - 1)-1:
#         return 2 * pow(pow(2, n - 1),2) + recur(n - 1, r - pow(2, n - 1), c)
#     elif r <= pow(2, n - 1)-1 and c > pow(2, n - 1)-1:
#         return 1 * pow(pow(2, n - 1),2) + recur(n - 1, r, c - pow(2, n - 1))
#     else:
#         return recur(n - 1, r, c)


# n, r, c = list(map(int, input().split(" ")))
# answer = recur(n, r, c) - 1
# print(answer)


def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n / 2, x, y)
    solve(n / 2, x, y + n / 2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n / 2, y + n / 2)


result = 0
N, X, Y = map(int, input().split(" "))
solve(2 ** N, 0, 0)

