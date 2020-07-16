arr = sorted(list(map(int, input().split())))
temp = set(arr)
if len(temp) == 3:
    print(max(arr) * 100)
elif len(temp) == 2:
    print(arr[1] * 100 + 1000)
    # count = [0] * 7
    # for i in range(len(arr)):
    #     count[arr[i]] += 1
    # for i in range(len(count)):
    #     if count[i] == 2:
    #         print(i * 100 + 1000)
else:
    print(arr[0] * 1000 + 10000)

