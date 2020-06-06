from collections import deque

def BFS(now, depth):
    global g, u, d
    count = 0
    dq = deque([[now, depth]])

    while dq:
        temp, count = dq.popleft()
        if visited[temp] == False:
            visited[temp] = True
            if temp == g:
                return count
            up = temp + u
            down = temp - d

            if visited[up] == False and up <= f:
                dq.append([up, count + 1])
            if visited[down] == False and down > 0:
                dq.append([down, count + 1])
    return -1

f, s, g, u, d = list(map(int, input().split()))
visited = [False] * 1000001
answer = 1e9
result = BFS(s, 0)
if result != -1:
    print(result)
else:
    print("use the stairs")
