# https://www.acmicpc.net/problem/17269
n, m = map(int, input().split())

# ord('문자열') - 65
alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a, b = input().split(" ")
ab = ""
min_len = min(n, m)
# ab_i = [0] * (n + m)
for i in range(min_len):
    ab += a[i] + b[i]

# if n == min_len:
#     for i in range(min_len, m):
#         ab += b[i]
# else:
#     for i in range(min_len, n):
#         ab += a[i]
ab += a[min_len:] + b[min_len:]

ab_i = [alpha[ord(i) - 65] for i in ab]
# for i in range(n + m):
#     ab_i[i] = alpha[ord(ab[i]) - 65]

# length = len(ab_i)
# while length > 2:
#     for i in range(length - 1):
#         ab_i[i] = (ab_i[i] + ab_i[i + 1]) % 10
#     length -= 1

# if ab_i[0] == 0:
#     print(ab_i[1], end="")
#     print("%")
# else:
#     for i in range(2):
#         print(ab_i[i], end="")
#     print("%")

for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        ab_i[j] += ab_i[j + 1]

print("{}%".format(ab_i[0] % 10 * 10 + ab_i[1] % 10))
