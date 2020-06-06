# import math

# num = input()
# length = len(num)
# num = int(num)
# li = []
# s = ""

# for i in range(length):
#     li.append(num % 10)
#     num = math.trunc(num / 10)

# li = sorted(li, reverse=True)

# for i in li:
#     s+=str(i)
# print(s)

a= input()

for i in range(9,-1,-1):
    for j in a:
        if int(j) == i:
            print(i,end='')
