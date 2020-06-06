def solution(n, s):
    answer = []
    if n>s:
        answer.append(-1)
        print(answer)
        return answer
    elif n == s:
        for i in range(n):
            answer.append(1)
            print(answer)
            return answer

    temp , rest = divmod(s,n)
    # temp = (s/n)
    # rest = s%n
    for i in range(n):
        if rest != 0:
            answer.append(temp+1)
            rest = rest - 1
        else:
            answer.append(temp)
    
    answer.sort()
    print(answer)
    return answer

solution(2,8)