# https://www.acmicpc.net/problem/9037
testcase = int(input())

def check():
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = arr[i] + 1
    return len(set(arr))


for i in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    cir = 0
    count = check()

    while count != 1:
        addV = []
        for i in range(len(arr)):
            addV.append(arr[i] // 2)
            arr[i] = arr[i] // 2
        for i in range(len(arr)):
            arr[i] += addV[i - 1]
        cir += 1
        count = check()
    print(cir)
