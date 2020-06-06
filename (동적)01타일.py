n = int(input())
li = [0]*n
li[0] = 1
li[1] = 2

for i in range(2,n):
    li[i] = (li[i-1] + li[i-2]) % 15746

result = li[n-1]
print(result)

# n = int(input())
# li = []
# li.append(1)
# li.append(2)

# for i in range(2,n):
#     temp = (li[i-1] + li[i-2]) % 15746
#     li.append(temp)

# result = li[n-1]
# print(result)
