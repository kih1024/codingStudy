import operator

n = int(input())
dic = {}

for _ in range(n):
    title = input()
    if title in dic:
        dic[title] = dic[title] + 1
    else:
        dic[title] = 1

target = max(dic.values())
array = []

for book, number in dic.items():
    if number == target:
        array.append(book)

print(sorted(array)[0])

# sdict = sorted(dic.items(), key=operator.itemgetter(0))
# sdict = sorted(sdict, key=lambda x: x[1], reverse=True)
# print(sdict[0][0])

