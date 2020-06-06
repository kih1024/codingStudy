# https://www.acmicpc.net/problem/9663
def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        row[x] = i
        if check(x):
            dfs(x + 1)


n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)

# def isAvailable(current_col, current_queen):
#     current_row = len(current_queen)
#     for queen_row in range(current_row):
#         if (
#             current_queen[queen_row] == current_col
#             or abs(current_queen[queen_row] - current_col) == current_row - queen_row
#         ):
#             return False
#     return True


# def dfs(current_row, current_queen):
#     global result
#     if current_row == n:
#         result += 1
#         return

#     for i in range(n):
#         current_col = i
#         if isAvailable(current_col, current_queen):
#             current_queen.append(current_col)
#             dfs(current_row + 1, current_queen)
#             current_queen.pop()


# n = int(input())

# result = 0
# dfs(0, [])
# print(result)
