# n = int(input())
# li = []
# tempL = []
# answer = []
# pivot = 0
# for i in range(n):
#     temp = int(input())
#     li.append(temp)

# for i in range(n):
#     if li[i] > pivot:
#         for j in range(pivot+1,li[i]+1):
#             tempL.append(j)
#             answer.append('+')
#             pivot+=1

#     if tempL[-1] == li[i]:
#         value = tempL.pop()
#         answer.append('-')
#     else:
#         print('NO')
#         exit(0)


# print('\n'.join(answer))
n = int(input())

pivot = 1
stack = []
answer = []

for i in range(1, n+1):
    data = int(input())
    while pivot <= data:
        stack.append(pivot)
        pivot+=1
        answer.append('+')
    if stack[-1] == data:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))