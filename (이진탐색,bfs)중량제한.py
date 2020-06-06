from collections import deque

def bfs(mid):
    queue = deque([s_node])
    visited = [False] * (n+1)
    visited[s_node] = True

    while queue:
        x = queue.popleft()
        for y,c in array[x]:
            if visited[y] == False and c >= mid:
                visited[y] = True
                queue.append(y)
    return visited[e_node]


n, m = map(int, input().split(" "))
li = []
start = 1000000000
end = 1
array = [[] for _ in range(n+1)]
result = 0
for _ in range(m):
    x,y,c = map(int, input().split(" "))
    array[x].append((y,c))
    array[y].append((x,c))
    start=min(start,c)
    end=max(end,c)

s_node, e_node = map(int, input().split(" "))

while start <= end:
    mid = (start+end) // 2
    if bfs(mid):
        result = mid
        mid += 1
        start = mid
    else:
        mid -= 1
        end = mid
print(result)
