import sys

sys.setrecursionlimit(100000)


def dfs(depth, oper, r, c):
    cl, rl = 0, 0
    if A[row][col] == k:
        return depth

    if depth > 100:
        return -1

    if oper == "R":
        for i in range(r):
            count = []
            di = dict()
            temp = []
            for j in range(c):
                if A[i][j] != 0:
                    if A[i][j] not in di:
                        di[A[i][j]] = 1
                    else:
                        di[A[i][j]] += 1
            for j in di.keys():
                # j는 키 di[j]는 키값(갯수)
                count.append((di[j], j))
            count.sort()
            for j in count:
                temp.append(j[1])
                temp.append(j[0])

            tt = min(len(temp), 100)
            cl = max(cl, tt)
            for j in range(tt):
                A[i][j] = temp[j]

            if tt < c:
                if tt - 1 >= 0:
                    for j in range(tt, c):
                        A[i][j] = 0

        if r < cl:
            return dfs(depth + 1, "C", r, cl)
        else:
            return dfs(depth + 1, "R", r, cl)

    else:
        for i in range(c):
            count = []
            di = dict()
            temp = []
            for j in range(r):
                if A[j][i] != 0:
                    if A[j][i] not in di:
                        di[A[j][i]] = 1
                    else:
                        di[A[j][i]] += 1
            for j in di.keys():
                # j는 키 di[j]는 키값(갯수)
                count.append((di[j], j))
            count.sort()
            for j in count:
                temp.append(j[1])
                temp.append(j[0])

            tt = min(len(temp), 100)
            rl = max(rl, tt)
            for j in range(tt):
                A[j][i] = temp[j]

            if tt < r:
                if tt - 1 >= 0:
                    for j in range(tt, r):
                        A[j][i] = 0

        if rl < c:
            return dfs(depth + 1, "C", rl, c)
        else:
            return dfs(depth + 1, "R", rl, c)


row, col, k = map(int, input().split())
row, col = row - 1, col - 1
A = [[0] * 100 for i in range(100)]
arr = [list(map(int, input().split())) for i in range(3)]
for i in range(3):
    for j in range(3):
        A[i][j] = arr[i][j]

print(dfs(0, "R", 3, 3))
