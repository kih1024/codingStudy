def func(r,c):
    result = []
    case = [fw,fb]

    for cc in case:
        temp = 0
        for i in range(r,r+8):
            for j in range(c,c+8):
                if b[i][j] != cc[i-r][j-c]:
                    temp+=1
        result.append(temp)
    return min(result)
        

N,M = map(int,input().split())
b = [list(input()) for _ in range(N)]
ans = 1e9
dy,dx = [0,1],[1,0]
fw = [[0]*8 for _ in range(8)]
fb = [[1]*8 for _ in range(8)]

for i in range(N):
    for j in range(M):
        if b[i][j] == 'W':
            b[i][j] = 1
        else:
            b[i][j] = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            fw[i][j] = 1
            fb[i][j] = fw[i][j]^1

for i in range(N):
    if i+7 >= N:
        break
    for j in range(M):
        if j+7 >= M:
            break
        ans = min(ans,func(i,j))

print(ans)