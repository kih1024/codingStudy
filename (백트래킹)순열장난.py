def ck(mv):
    for i in range(1, mv + 1):
        if not visited[i]:
            return False
    return True


def dfs(depth, mv):
    global isFind
    if depth >= len(arr):
        if ck(mv):
            isFind = True
        return

    if arr[depth] == 0:
        return

    for i in range(2):
        if i == 1 and depth + 1 <= len(arr) - 1:
            newN = int(str(arr[depth]) + str(arr[depth + 1]))
            if newN > 50:
                continue
            if not visited[newN]:
                visited[newN] = True
                max_value = max(mv, newN)
                answer.append(newN)
                dfs(depth + 2, max_value)
                if isFind:
                    return
                visited[newN] = False
                answer.pop()
        elif not visited[arr[depth]]:
            newN = arr[depth]
            visited[newN] = True
            max_value = max(mv, newN)
            answer.append(newN)
            dfs(depth + 1, max_value)
            if isFind:
                return
            visited[newN] = False
            answer.pop()


arr = list(map(int, input()))
visited = [False] * 51
isFind = False
answer = []

dfs(0, 0)
for i in range(len(answer)):
    answer[i] = str(answer[i])

print(" ".join(answer))
