def ck(A):
    # write your code in Python 3.6
    sign = [0] * (len(A) - 1)
    # 자신이 앞에 나무보다 크면 1 작으면 -1 같으면 0
    for i in range(len(A) - 1):
        sign[i] = A[i] - A[i + 1]
    print(sign)

    if 0 in sign:
        return False

    for i in range(len(sign) - 1):
        if sign[i] * sign[i + 1] > 0:
            return False

    return True


def solution(A):
    # write your code in Python 3.6
    temp = []
    count = 0
    if ck(A):
        return 0
    for i in A:
        temp = []
        for j in range(len(A)):
            if j == i:
                continue
            else:
                temp.append(A[j])
        if ck(temp):
            count += 1

    if count != 0:
        return count
    else:
        return -1
