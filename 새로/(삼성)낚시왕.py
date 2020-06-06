import sys

input = sys.stdin.readline
R,C,M = map(int,input().split())
arr = [[[0]*3 for j in range(C)] for i in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    arr[r-1][c-1] = [s,d-1,z]
dy, dx, ans = (-1, 1, 0, 0), (0, 0, 1, -1), 0

for t in range(C):
    for i in range(R):
        if arr[i][t] != [0,0,0]:
            _,_,z = arr[i][t]
            ans += z
            arr[i][t] = [0,0,0]
            break
    arr2 = [[[0]*3 for j in range(C)] for i in range(R)]

    for i in range(R):
        for j in range(C):
            s,d,z = arr[i][j]
            if z:
                if d < 2:
                    ss,dd,ii=s%((R-1)*2),d,i
                    for _ in range(ss):
                        if ii == 0 and dd == 0:
                            dd = 1
                        if ii == R-1 and dd == 1:
                            dd = 0
                        ii += dy[dd]
                    _,_,z2 = arr2[ii][j]
                    if z > z2:
                        arr2[ii][j] = [s,dd,z]
                    
                else:
                    ss,dd,jj=s%((C-1)*2),d,j
                    for _ in range(ss):
                        if jj == 0 and dd == 3:
                            dd = 2
                        if jj == C-1 and dd == 2:
                            dd = 3
                        jj += dx[dd]
                    _,_,z2 = arr2[i][jj]
                    if z > z2:
                        arr2[i][jj] = [s,dd,z]
    arr = arr2[:]

print(ans)

