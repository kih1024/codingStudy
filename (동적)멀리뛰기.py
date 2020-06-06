# from itertools import combinations
# import operator as op
# from functools import reduce
# def ncr(n,r):
#     if n<1 or r<0 or n<r:
#         raise ValueError
#     r = min(r, n-r)
#     numerator = reduce(op.mul,range(n,n-r,-1),1)
#     denominator = reduce(op.mul, range(1,r+1),1)
#     return numerator

# def countTwo(n):
#     count = 0
#     for i in range(n):
#         if i*2 > n:
#             break
#         count = i
#     return count


# def solution(n):
#     answer = 1
#     countOne = 0
#     temp = []
#     count = countTwo(n)
#     print(count)
#     for i in range(1,count+1):
#         countOne = n - i*2
#         answer+=ncr(i+countOne,i)
#         # for j in range(i+countOne):
#         #     temp.append(j)
#         # print(temp)
#         # print(len(list(combinations(temp,i))))
#         # answer+=len(list(combinations(temp,i)))
#         # # print(len(list(combinations(temp,j))))
#         # temp.clear()
#     answer=answer%1234567
#     print(answer)
#     return answer

# solution(3)

def solution(n):
    answer = 0
    dp = [0]*(n+1)
    print(dp)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    print(dp[n])
    answer = dp[n]
    return answer

solution(4)


def solution(num):
	result = [1, 2]
	i = 0
	while len(result) < num:
		result.append((result[i] + result[i+1]) % 1234567)
		i += 1

	return result[num-1]
