import heapq

def dijkstra():
    global M, N
    remove[(0, 0)] = 0
    q = []
    heapq.heappush(q, [remove[(0, 0)], (0, 0)])

    while q:
        current_remove, cur_node = heapq.heappop(q)

        if remove[cur_node] < current_remove:
            continue

        y, x = cur_node
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if arr[ny][nx] == 1:
                new_remove = current_remove + 1
            else:
                new_remove = current_remove

            if new_remove < remove[(ny, nx)]:
                remove[(ny, nx)] = new_remove
                heapq.heappush(q, [remove[(ny, nx)], (ny, nx)])

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
remove = {(i, j): 1e9 for j in range(M) for i in range(N)}
dijkstra()
print(remove)
print(remove[(N-1,M-1)])

