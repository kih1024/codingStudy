def DFS(oper, operL):
    if sum(oper) == 0:
        temp = num[0]
        for i in range(len(operL)):
            if operL[i] == 0:
                temp += num[i + 1]
            elif operL[i] == 1:
                temp -= num[i + 1]
            elif operL[i] == 2:
                temp *= num[i + 1]
            else:
                if temp < 0:
                    temp = -temp // num[i + 1]
                    temp = -temp
                else:
                    temp = temp // num[i + 1]

        result.append(temp)

    for i in range(len(oper)):
        if oper[i] == 0:
            continue
        operL.append(i)
        oper[i] -= 1
        DFS(oper, operL)
        operL.pop()
        oper[i] += 1

N = int(input())
num = list(map(int, input().split()))
operation = list(map(int, input().split()))
result = []
DFS(operation, [])

print(max(result))
print(min(result))
