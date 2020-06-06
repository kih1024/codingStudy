test_case = int(input())

for _ in range(test_case):
    result = 0
    n, m = list(map(int, input().split(" ")))
    queue = list(map(int, input().split(" ")))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    while True:
        isMax = True
        # if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
        for i in range(1, len(queue)):
            if queue[0][0] < queue[i][0]:
                temp = queue.pop(0)
                queue.append(temp)
                isMax = False
                break
        if isMax:
            result = result + 1
            temp = queue.pop(0)
            if temp[1] == m:
                print(result)
                break

