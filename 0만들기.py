#eval 함수를 사용
mark = []

def recur(sign, count):
    global n
    global mark

    mark.append(sign)

    if count == n-1:
        string = ""
        for i in range(n-1):
            string += str(i+1) + mark[i]
        string += str(n)

        if eval(string.replace(' ', '')) == 0:
            print(string)
            mark.pop()
            return
        mark.pop()
        return

    recur(' ', count+1)
    recur('+', count+1)
    recur('-', count+1)
    mark.pop()


testcase = int(input())

for _ in range(testcase):
    n = int(input())
    recur(' ', 1)
    recur('+', 1)
    recur('-', 1)
    print()


