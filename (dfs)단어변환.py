min2 = 1000

def dfs(begin,target,words,history=[],depth=0):
    global min2
    print(begin,history)
    count = 0 

    if begin == target:
        min2 = min(min2,depth)
        return

    for index in range(len(words)):
        count = 0
        for j in range(len(begin)):
            if begin[j] != words[index][j]:
                count=count+1
        if count != 1 :
            continue

        if words[index] not in history and count == 1:
            history.append(words[index])
            dfs(words[index],target,words,history,depth+1)
            history.pop(-1)

    return

    
               
def solution(begin, target, words):
    answer = 0
    global min2
    if target not in words:
        print(0)
        return 0
    dfs(begin,target,words)

    print(min2)
    answer = min2
    return answer

solution("hit","cog",["hot", "dot", "dog", "lot", "log","cog"])





















# def dfs(now, target, words, history=[], depth=0):
#     global min_
#     print(now, history)
#     if now == target:
#         min_ = min(min_, depth)

#     if depth >= min_:
#         return

#     for word in words:
#         if word in history:
#             continue
#         cnt = 0
#         for i in range(len(target)):
#             if word[i] != now[i]:
#                 cnt += 1
#             if cnt > 1:
#                 break
#         if cnt == 1 and word not in history:
#             history.append(word)
#             dfs(word, target, words, history, depth+1)
#             history.pop(-1)

# min_ = 51
# def solution(begin, target, words):
#     global min_
#     if target not in words:
#         return 0
#     dfs(begin, target, words)
#     return min_

# solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])