def solution(numbers, hand):
    answer = ''
    ln = [1,4,7]
    rn = [3,6,9]
    nowL,nowR = 9,11

    b = [[(i+1)+j*3 for i in range(3)] for j in range(3)]
    b.append([-1,0,-2])
    print(b)

    for i in numbers:
        if i in ln:
            nowL = i-1
            answer+="L"
        elif i in rn:
            nowR = i-1
            answer+="R"
        else:
            if i == 0:
                nowP = 10
            else:
                nowP = i - 1
            r,c = nowP//3,nowP%3
            lr,lc = nowL//3,nowL%3
            rr,rc = nowR//3,nowR%3
            left = abs(r-lr)+abs(c-lc)
            right = abs(r-rr)+abs(c-rc)
            if left < right:
                nowL = nowP
                answer+="L"
            elif right < left:
                nowR = nowP
                answer+="R"
            else:
                if hand == "left":
                    nowL = nowP
                    answer+="L"
                else:
                    nowR = nowP
                    answer+="R"
                
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))