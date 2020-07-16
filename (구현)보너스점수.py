n = int(input())
string = input()
bonus = 0
result = 0

for i in range(n):
    if string[i] == "O":
        result = result + (i + 1) + bonus
        bonus += 1
    else:
        bonus = 0
print(result)
