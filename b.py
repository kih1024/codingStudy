# z = 122, A =65
# ord
def solution(S, C):
    # write your code in Python 3.6
    li = []
    li2 = []
    temp = []
    first = []
    last = []
    result = []
    addV = dict()
    li = S.split("; ")
    for i in range(len(li)):
        temp2 = li[i].replace("-", "")
        temp = temp2.split(" ")
        first.append(temp[0].lower())
        last.append(temp[-1].lower())

    for i in range(len(li)):
        ss = f"{last[i]}_{first[i]}"
        if ss not in addV:
            addV[ss] = 1
            result.append(f"{li[i]} <{last[i]}_{first[i]}@{C.lower()}.com>")
        else:
            addV[ss] += 1
            result.append(f"{li[i]} <{last[i]}_{first[i]}{addV[ss]}@{C.lower()}.com>")
    print("; ".join(result))
    return "; ".join(result)


solution(
    "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker",
    "Example",
)
