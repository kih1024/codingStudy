def solution(n, costs):
    answer = 0
    visit = [costs[0][0]]
    sumV = 0

    # costs.sort(key=lambda x: x[2])
    costs.sort()
    while len(visit) != n:
        temp = 10000
        idx = 0
        for i in range(len(costs)):
            if costs[i][0] in visit or costs[i][1] in visit:
                if costs[i][0] in visit and costs[i][1] in visit:
                    continue
                if temp > costs[i][2]:
                    temp = costs[i][2]
                    idx = i
        answer += temp
        visit.append(costs[idx][0])
        visit.append(costs[idx][1])
        visit = list(set(visit))
        costs.pop(idx)
    print(answer)
    # print(answer)
    return answer


solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]])

