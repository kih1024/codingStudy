def solution(N, stages):
    answer = []
    stage_num = [0 for _ in range(N + 2)]
    length = len(stages)
    arr = []

    for i in stages:
        stage_num[i] += 1
    print(stage_num)
    for i in range(1, N + 1):
        if length == 0:
            arr.append((0, i))
        else:
            arr.append((stage_num[i] / length, i))
            length -= stage_num[i]

    print(arr)
    arr = sorted(arr, key=lambda x: x[0], reverse=True)
    for _, idx in arr:
        answer.append(idx)

    print(answer)
    return answer


solution(5, [2, 1, 2, 3, 3, 3, 2])
