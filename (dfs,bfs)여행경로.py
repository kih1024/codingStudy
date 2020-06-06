now = "ICN"
answer = []
def dfs(str,count):


def solution(tickets):
    answer.append("ICN")
    dup = []
    count = len(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] is now:
            dup.append(tickets[i][1])
    dup.sort(key=str.lower)
    answer.append(dup[0])
    tickets.remove([now,dup[0]])
    now = dup[0]
    dup.clear()


    
    # while len(tickets) != 0:
    #     for i in range(len(tickets)):
    #         if tickets[i][0] is now:
    #             dup.append(tickets[i][1])
    #     dup.sort(key=str.lower)
    #     answer.append(dup[0])
    #     tickets.remove([now,dup[0]])
    #     now = dup[0]
    #     dup.clear()
    print(answer)

    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])