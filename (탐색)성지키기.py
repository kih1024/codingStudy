n, m = list(map(int, input().split(" ")))
li = []
for i in range(n):
    t = input()
    li.append(t)

h = [0] * n
y = [0] * m
h_count = 0
y_count = 0
for i in range(n):
    for j in range(m):
        if li[i][j] == "X":
            h[i] = 1
            y[j] = 1

for i in range(n):
    if h[i] == 0:
        h_count += 1

for i in range(m):
    if y[i] == 0:
        y_count += 1

print(max(h_count, y_count))



# for i in range(n):
#     for j in range(m):
#         print(li[0][0])

# li = [0]*5

# print(li)

