def ck(t):
    global N
    for tt in t:
        r, c = tt[0], tt[1]
        # 0 1 2 3 : 동 남 서 북
        for i in range(4):
            if i == 0:
                for k in range(c + 1, N):
                    if arr[r][k] == "O":
                        break
                    if arr[r][k] == "S":
                        return False
            elif i == 1:
                for k in range(r + 1, N):
                    if arr[k][c] == "O":
                        break
                    if arr[k][c] == "S":
                        return False
            elif i == 2:
                for k in range(c - 1, -1, -1):
                    if arr[r][k] == "O":
                        break
                    if arr[r][k] == "S":
                        return False
            else:
                for k in range(r - 1, -1, -1):
                    if arr[k][c] == "O":
                        break
                    if arr[k][c] == "S":
                        return False
    return True

def DFS(o, idx_s):
    global N, ans
    if o == 3:
        if ck(t):
            ans = True
        return

    for i in range(idx_s, len(x) - (2 - o)):
        r, c = x[i][0], x[i][1]
        o += 1
        arr[r][c] = "O"
        DFS(o, i + 1)
        if ans:
            return
        o -= 1
        arr[r][c] = "X"


N = int(input())
arr = []
s, t, x = [], [], []
for i in range(N):
    temp = list(input().split())
    arr.append(temp)
    for j in range(N):
        if temp[j] == "T":
            t.append((i, j))
        elif temp[j] == "X":
            x.append((i, j))
ans = False
DFS(0, 0)

if ans:
    print("YES")
else:
    print("NO")