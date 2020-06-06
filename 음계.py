def solution(li):
    state = 0
    for i in range(len(li)-1):
        if li[i] < li[i+1]:
            if state == -1:
                return False
            state = 1
        elif li[i] > li[i+1]:
            if state == 1:
                return False
            state = -1
    return True


inputs = map(int,input().split())
li = list(inputs)
result = solution(li)

if result:
    if li[0] < li[1]:
        print("ascending")
    else:
        print("descending")
else:
    print("mixed")


