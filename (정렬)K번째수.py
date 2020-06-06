n, k = list(map(int, input().split(" ")))
a= list(map(int,input().split(' ')))

a = sorted(a)
print(a[k-1])
# for i in range(len(a)):
#     if i==k-1:
#         print(a[i])
