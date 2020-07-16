# 원래 인덱스를 가지고 있어야 하는경우 리스트안에 튜블형태로 보관하자.
def solution(dataSource, tags):
    answer = []
    count = [[0, i] for i in range(100)]
    for i in range(len(dataSource)):
        for j in range(len(tags)):
            if tags[j] in dataSource[i]:
                count[i][0] += 1

    count.sort(key=lambda x: x[0], reverse=True)
    minV = min(len(dataSource), 10)
    for i in range(minV):
        print(dataSource[count[i][1]][0])
        if count[i][0] != 0:
            answer.append(dataSource[count[i][1]][0])
    print(answer)
    return answer


solution(
    [
        ["doc1", "t1", "t2", "t3"],
        ["doc2", "t0", "t2", "t3"],
        ["doc3", "t1", "t6", "t7"],
        ["doc4", "t1", "t2", "t4"],
        ["doc5", "t6", "t100", "t8"],
    ],
    ["t1", "t2", "t3"],
)
