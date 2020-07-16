def longest(arr):
    temp = "".join(arr)
    li = list(temp.split("0"))
    maxV = 0
    total = 0
    count = []
    for i in li:
        total += len(i)
        maxV = max(maxV, len(i))

    return total + (maxV ** 2)


def solution(answer_sheet, sheets):
    dp = [1] * len(answer_sheet)
    result = []
    # i는 각각의 답변들
    for i in range(len(sheets) - 1):
        for j in range(i + 1, len(sheets)):
            arr = []
            for k in range(len(answer_sheet)):
                if sheets[i][k] == sheets[j][k] and sheets[i][k] != answer_sheet[k]:
                    arr.append(sheets[i][k])
                else:
                    arr.append("0")
            result.append(longest(arr))

    # answer = -1
    return max(result)


solution(
    "4132315142", ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]
)
