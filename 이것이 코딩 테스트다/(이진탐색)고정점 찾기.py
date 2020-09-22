def bisec(s, e):
    if s > e:
        return -1
    mid = (s + e) // 2

    if mid == arr[mid]:
        return mid

    # 중간점이 가리키는 값보다 중간점이 작은 경우 왼쪽 확인
    if arr[mid] > mid:
        return bisec(s, mid - 1)
    # 중간점이 가리키는 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return bisec(mid + 1, e)


N = int(input())
arr = list(map(int, input().split()))

ans = bisec(0, N - 1)

print(ans)

