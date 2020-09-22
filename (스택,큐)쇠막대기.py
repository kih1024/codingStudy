# def binary_search(data, idx):
#     print(data, idx)
#     if data[0] > idx:
#         return data[0]
#     # if len(data) == 1:
#     #     return

#     medium = len(data) // 2
#     if data[medium] < idx:
#         return binary_search(data[medium :], idx)
#     else:
#         return binary_search(data[:medium], idx)


# def solution(arrangement):
#     answer, i = 0, 0
#     lazer, pipe = [], []
#     arrangement = arrangement.replace("()", "L")
#     length = len(arrangement)
#     while i < length:
#         if arrangement[i] == "L":
#             lazer.append(i)
#         elif arrangement[i] == "(":
#             pipe.append(i)
#         else:
#             idx = pipe.pop()
#             spliteN = 1
#             # 이진 탐색 이용
#             # print("==========================")
#             # binary_search(lazer, idx)
#             for l in range(len(lazer)-1,-1,-1):
#                 if idx < l:
#                     spliteN += 1
#             answer += spliteN
#         i += 1
#     print(answer)
#     return answer


# def solution(arrangement):
#     answer, i = 0, 0
#     lazer, pipe = [], []
#     arrangement = arrangement.replace("()", "R")
#     length = len(arrangement)
#     while i < length:
#         if arrangement[i] == "R":
#             lazer.append(i)
#         elif arrangement[i] == "(":
#             pipe.append(i)
#         else:
#             idx = pipe.pop()
#             spliteN = 1
#             for l in range(len(lazer) - 1, -1, -1):
#                 if idx < lazer[l]:
#                     spliteN += 1
#                 else:
#                     break
#             answer += spliteN
#         i += 1
#     print(answer)
#     return answer
# def solution(arrangment):
#     arrangement = arrangment.replace("()", "0")
#     x = 0
#     cnt = 0
#     for e in arrangement:
#         if e == "(":
#             x += 1
#             cnt += 1
#         elif e == "0":
#             cnt += x
#         else:
#             x -= 1
#     return cnt


# def solution(arrangement):
#     arrangement = list(arrangement)
#     temp = list()
#     x = 0
#     cnt = 0
#     for i in range(len(arrangement)):
#         a = arrangement.pop(0)
#         if a == "(":
#             x += 1
#             cnt += 1
#         else:
#             if temp[-1] == "(":
#                 x -= 1
#                 cnt -= 1
#                 cnt += x
#             else:
#                 x -= 1
#         temp.append(a)
#         print(i, x, cnt)
#     return cnt

# def solution(arrangment) :
#     arrangement = arrangment.replace("()","0")
#     x = 0;cnt = 0;
#     for e in arrangement :
#         if e == "(" : x+=1; cnt+=1
#         elif e == "0" : cnt+=x
#         else : x-=1
#     return cnt

# cutN : 잘린 막대기 수
# num : 잘리지 않은 원래 막대기 수

def solution(arrangment):
    arr = arrangment.replace("()", "L")
    cutN, num = 0, 0

    for i in arr:
        if i == "(":
            cutN += 1
            num += 1
        elif i == ")":
            num -= 1
        else:
            cutN += num
    print(cutN)
    return cutN

s = input()
solution(s)
