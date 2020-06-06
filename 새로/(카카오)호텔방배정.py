class Node(object):
    def __init__(self, parent):
        self.parent = parent

def solution(k, room_number):
    answer = []
    client = [0]*len(room_number)
    room_ck = dict()

    for i in range(len(room_number)):
        n = room_number[i]
        if n not in room_ck:
            room_ck[n] = Node(n+1)
            client[i] = n
        else:
            temp = []
            while True:
                temp.append(n)
                p = room_ck[n].parent
                if p not in room_ck:
                    room_ck[p] = Node(p+1)
                    client[i] = p
                    for k in temp:
                        room_ck[k].parent = p+1
                    break
                else:
                    n = room_ck[p].parent
                    if n not in room_ck:
                        room_ck[n] = Node(n+1)
                        client[i] = n
                        for k in temp:
                            room_ck[k].parent = n+1
                        break
    return client


print(solution(10,[1,3,4,1,3,1]))