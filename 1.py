def solution(inputString):
    answer = -1
    arr = [False] * 4
    count = [0] * 4
    figure = [("(", ")"), ("{", "}"), ("[", "]"), ("<", ">")]
    for i in range(len(inputString)):
        for j in range(len(figure)):
            if inputString[i] == figure[j][0]:
                arr[j] = True
                break

            if inputString[i] == figure[j][1] and arr[j] == True:
                count[j] += 1
                arr[j] = False
                break

    for i in arr:
        if i == True:
            return -1

    answer = sum(count)
    return answer


ans = solution(">_<")
print(ans)
