def solution(p):
    answer = 0
    while True:
        p += 1
        tt = p
        temp = []
        count = 0
        while True:
            count += 1
            n = tt % 10
            tt = tt // 10
            temp.append(n)
            if tt == 0:
                break
        if count == len(set(temp)):
            break

    answer = p
    return answer


print(solution(2015))
