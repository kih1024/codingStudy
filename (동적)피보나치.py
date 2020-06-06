li = [0, 1]

n = int(input())

for i in range(2,n+1):
    temp = li[i-1] + li[i-2]
    li.append(temp)

print(li[n])
