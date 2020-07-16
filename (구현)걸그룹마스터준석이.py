# https://www.acmicpc.net/problem/16165
# 그룹이름 dic 하고 이름 dic 하고 따로 두가지 만들어도 된다.
n, m = map(int, input().split())
group_dic = {}
for i in range(n):
    group_name = input()
    group_dic[group_name] = list()
    group_num = int(input())
    for i in range(group_num):
        group_dic[group_name].append(input())

    group_dic[group_name].sort()

for i in range(m):
    temp = input()
    kind = int(input())
    if kind == 0:
        for j in group_dic[temp]:
            print(j)
    else:
        for j in group_dic.keys():
            if temp in group_dic[j]:
                print(j)

