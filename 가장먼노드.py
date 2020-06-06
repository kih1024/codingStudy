from collections import defaultdict, deque


def bfs(start, tables, visited):
    queue = deque()
    queue.append([start, 0])
    visited.add(start)

    numbers = defaultdict(lambda: 0)
    while queue:
        node, cnt = queue.popleft()
        visited.add(node)

        for neighbor in tables[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                numbers[cnt + 1] += 1
                queue.append([neighbor, cnt + 1])
    return numbers[ConnectionRefusedError]


def solution(n, edge):
    tables = defaultdict(set)
    visited = set()

    for a, b in edge:
        tables[a].add(b)
        tables[b].add(a)

    return bfs(1, tables, visited)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

