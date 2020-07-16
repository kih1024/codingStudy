from collections import deque
from copy import deepcopy

# 
def back(r,c,res,now,v):
    # print(r,c,res,now)
    # for i in range(10):
    #         print(v[i])
    global valid
    global result
    if now == count:
        valid = True
        result = min(result,res)
        return
    for i in range(5):
        isValid = True
        if paper[i+1] >= 5:
            continue
        for j in range(3):
            y = r + dy[j]*i
            x = c + dx[j]*i
            if y > 9 or x > 9 or v[y] == True or arr[y][x] == 0:
                isValid = False
                break
            if i == 0:
                break
        if not isValid:
            continue
        nc = (i+1)*(i+1) + now
        nxt = (r*10) + (c + i) + 1
        visit = deepcopy(v)
        visit[r][c] = 1
        paper[i+1] += 1
        for j in range(3):
            for k in range(1,i+1):
                visit[r + dy[j]*k][c + dx[j]*k] = 1

        for z in range(nxt,100):
            ii = z // 10
            jj = z % 10
            if visit[ii][jj] == 0 and arr[ii][jj] == 1:
                # print(ii,jj)
                back(ii, jj,res+1,nc,visit)
        paper[i+1] -= 1

arr = [list(map(int, input().split())) for i in range(10)]
visited = [[0] * 10 for i in range(10)]
dy, dx = [0, 1, 1], [1, 1, 0]
paper = [0] * 6
result= 1e9
count = 0
isFirst = True
valid = False
for i in range(100):
    r = i // 10
    c = i % 10
    if arr[r][c] == 1:
        if isFirst:
            fr,fc = r,c
            isFirst = False
        count += 1
back(fr,fc,1,1,visited)
if valid:
    print(result)
else:
    print(-1)