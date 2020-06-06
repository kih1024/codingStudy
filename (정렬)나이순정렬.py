n = int(input())
li = []
for i in range(n):
    age, name = input().split(" ")
    li.append((int(age), name))

li = sorted(li, key=lambda x: x[0])
for i in range(len(li)):
    print(li[i][0], li[i][1])
