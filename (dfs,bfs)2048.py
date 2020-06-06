# https://www.acmicpc.net/problem/12100
# import sys
# sys.setrecursionlimit(100000)

# dfs 를 이용한다. bfs 를 이용
# 한방향 정하고 돌려서 풀어본다 (90도 돌리는것은 b[i][j] 는 nb[j][n-1-i]로 간다)
# 돌리지 않고 4방향 다 구현해 본다. 여기서는 왼쪽으로 미는 방향으로 풀음
# >>> A = [[1,2,3],[4,5,6]] 참고 :http://pyengine.blogspot.com/2014/03/python-zip.html
# >>> list( zip(*A))
def move(l):
    # 사전에 미리 왼쪽에서부터 빈칸 없이 리스트를 저장
    new_list = [i for i in l if i]
    for i in range(1, len(new_list)):
        if new_list[i - 1] == new_list[i]:
            new_list[i - 1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (n - len(new_list))


def rotate90(m):
    nm = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nm[j][n - i - 1] = m[i][j]
    return nm


def dfs(m, count):
    maxV = max([max(i) for i in m])
    if count == 5:
        return maxV

    for _ in range(4):
        nm = [move(i) for i in m]
        if nm != m:
            maxV = max(maxV, dfs(nm, count + 1))
        m = rotate90(m)

    return maxV


n = int(input())
arr = [list((map(int, input().split()))) for i in range(n)]
print(dfs(arr, 0))
