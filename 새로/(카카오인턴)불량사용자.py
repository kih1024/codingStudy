# https://sj602.github.io/2020/04/05/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B6%88%EB%9F%89-%EC%82%AC%EC%9A%A9%EC%9E%90/

from copy import deepcopy

def dfs(candidates, users, result):
    if not candidates:
        results.add(tuple(sorted(result)))
        return

    new_candidates = deepcopy(candidates)
    curr = new_candidates.pop()
    for item in curr:
        if item in users:
            new_result = deepcopy(result)
            new_result.append(item)
            new_users = deepcopy(users)
            new_users.remove(item)

            dfs(new_candidates, new_users, new_result)


answer = 0

results = set()
def solution(u, b):
    global answer
    candidates = []
    for i in range(len(b)):
        temp = []
        for j in range(len(u)):
            if len(b[i]) != len(u[j]):
                continue
            isValid = True
            if b[i] != "*" * len(u[j]):
                for k in range(len(b[i])):
                    if b[i][k] == "*":
                        continue
                    if b[i][k] != u[j][k]:
                        isValid = False
                        break
            if isValid:
                temp.append(u[j])
        candidates.append(temp)
    print(candidates)
    dfs(candidates, u, [])
    print(len(results))
    return len(results)


# import copy




# def solution(user_id, banned_id):
#     candidates = []

#     for bid in banned_id:
#         temp = []
#         for uid in user_id:
#             found = True
#             if len(bid) != len(uid):
#                 continue
#             for i in range(len(bid)):
#                 if bid[i] == "*" or bid[i] == uid[i]:
#                     continue
#                 else:
#                     found = False
#                     break

#             if found:
#                 temp.append(uid)

#         candidates.append(temp)

#     results = set()
#     dfs(candidates, user_id, [], results)

#     return len(results)


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"],
))
