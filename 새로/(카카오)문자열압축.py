# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
def solution(s):
    answer = len(s)
    dup = len(s) // 2
    for k in range(1, dup + 1):
        is_duplicated = False
        temp = ""
        count = 1
        i = 0
        while i < len(s):
            if s[i : i + k] == s[i + k : i + k + k]:
                is_duplicated = True
                count += 1
            else:
                if is_duplicated:
                    temp += f"{count}{s[i:i+k]}"
                    count = 1
                    is_duplicated = False

                else:
                    temp += s[i : i + k]
                    count = 1
                    is_duplicated = False
            i += k
        answer = min(answer, len(temp))
    return answer


print(solution("aabbaccc"))

# def solution(s):
#     answer = len(s)
#     dup = len(s) // 2
#     is_duplicated = False
#     for k in range(1, dup + 1):
#         dic = []
#         print("--------------------------")
#         print(f"길이가 {k}")
#         temp = ""
#         count = 1
#         i = 0
#         while i < len(s):
#             if s[i : i + k] == s[i + k : i + k + k]:
#                 for i in dic:
#                     if i[0] == s[i : i + k]:
#                         isFind = True
#                         i[1]+=1
#                         break
#                 if not isFind:
#                     dic.append([s[i : i + k],1])


#                 if [s[i : i + k],*] in dic:
#                     dic[s[i : i + k]] += 1
#                 else:
#                     dic[s[i : i + k]] = 1
#                 i+=k
#             else:
#                 i+=k
#         print(temp)
#         answer = min(answer, len(temp))
#     return answer


# print(solution("abcabcdede"))

# an = [["asd",1]]
# if ["asd",] in an:
#     print(an)
