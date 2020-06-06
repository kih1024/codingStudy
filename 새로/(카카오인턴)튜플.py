# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = s.replace("{{", "").replace("}}", "").split("},{")
    t = []
    for ss in s:
        t.append(list(map(int, ss.split(","))))
    t = sorted(t, key=lambda x: len(x))
    # print(t)
    for i in range(len(t)):
        for j in range(i+1):
            if t[i][j] not in answer:
                answer.append(t[i][j])
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
