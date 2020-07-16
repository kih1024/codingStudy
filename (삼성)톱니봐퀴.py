def rotate(li):
    for i in range(4):
        if li[i] == -1:
            temp = arr[i][0]
            arr[i][0:7] = arr[i][1:]
            arr[i][-1] = temp
        elif li[i] == 1:
            temp = arr[i][-1]
            arr[i][1:] = arr[i][0:7]
            arr[i][0] = temp

def process(num, direction):
    isRotate = [0, 0, 0, 0]
    isRotate[num] = direction
    # 왼쪽
    temp = direction
    for i in range(num - 1, -1, -1):
        if arr[i][2] == arr[i + 1][6]:
            break
        else:
            temp = -temp
            isRotate[i] = temp

    # 오른쪽
    temp = direction
    for i in range(num + 1, 4):
        if arr[i][6] == arr[i - 1][2]:
            break
        else:
            temp = -temp
            isRotate[i] = temp
    rotate(isRotate)

arr = [list(map(int, list(input()))) for i in range(4)]
k = int(input())
score = [1, 2, 4, 8]
result = 0
for i in range(k):
    num, direction = map(int, input().split())
    process(num - 1, direction)

for i in range(len(arr)):
    if arr[i][0] == 1:
        result += score[i]

print(result)
