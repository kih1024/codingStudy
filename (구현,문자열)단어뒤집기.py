s = input()
temp = ""
ck = False
result = ""

for i in s:
    if i == " ":
        if not ck:
            result += temp[::-1] + " "
            # print(temp[::-1], end=" ")
            temp = ""
        else:
            result += " "
            # print(" ", end="")
    elif i == "<":
        result += temp[::-1] + "<"
        # print(temp[::-1] + "<", end="")
        temp = ""
        ck = True
    elif i == ">":
        result += ">"
        # print(">", end="")
        ck = False
    else:
        if ck:
            result += i
            # print(i, end="")
        else:
            temp += i

result += temp[::-1]
# print(temp[::-1], end="")
print(result)
