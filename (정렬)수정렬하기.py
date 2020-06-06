n = int(input())

li = []

for _ in range(n):
    k = int(input())
    li.append(k)

li=sorted(li)

for i in range(n):
    print(li[i])