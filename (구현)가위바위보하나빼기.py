# https://www.acmicpc.net/problem/16675
ml, mr, tl, tr = ("SRP".index(i) for i in input().split())

if ml == mr and (ml + 1) % 3 in [tl, tr]:
    print("TK")
elif tl == tr and (tl + 1) % 3 in [ml, mr]:
    print("MS")
else:
    print("?")
# def game(a, b):
#     if a == "S":
#         if b == "S":
#             return "?"
#         if b == "R":
#             return "TK"
#         if b == "P":
#             return "MS"
#     elif a == "R":
#         if b == "S":
#             return "MS"
#         if b == "R":
#             return "?"
#         if b == "P":
#             return "TK"
#     else:
#         if b == "S":
#             return "TK"
#         if b == "R":
#             return "MS"
#         if b == "P":
#             return "?"

# m = [0] * 2
# t = [0] * 2

# m[0], m[1], t[0], t[1] = input().split()

# if len(set(m)) == 1 and len(set(t)) == 1:
#     print(game(m[0], t[0]))
# elif len(set(m)) == 1 and len(set(t)) == 2:
#     temp = []
#     temp.append(game(m[0], t[0]))
#     temp.append(game(m[0], t[1]))
#     if "TK" in temp:
#         print("TK")
#     else:
#         print("?")
# elif len(set(m)) == 2 and len(set(t)) == 1:
#     temp = []
#     temp.append(game(m[0], t[0]))
#     temp.append(game(m[1], t[0]))
#     if "MS" in temp:
#         print("MS")
#     else:
#         print("?")
# else:
#     print("?")

