n = int(input())
li = []

for _ in range(n):
    x, y = input().split(" ")
    li.append((int(x), int(y)))
# li = sorted(li, key=lambda x: (x[0], x[1]))
li = sorted(li) # 파이썬의 sorted는 기본적으로 모든 속성에 대해 오른차순으로 정렬하는 성질이 있음.

for i in li:
    print(i[0], i[1])

