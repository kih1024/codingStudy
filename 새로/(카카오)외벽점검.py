# https://biewoom.github.io/coding%20test/kakao%202020%20blind/2020/04/17/wall.html

from itertools import permutations

def ck(n,weak,num,f_pos):
    wall = [0] * n
    # 시작 위치 고르기
    for p in f_pos:
        print(f"그때 p {p}")
        for start in range(len(weak)):
            _left = weak[:start]; _right = weak[start:]
            traverse_list = _right + [x+n for x in _left]
            candidate = list(p).copy()
            # print(candidate)
            while traverse_list and candidate:
                cur = traverse_list.pop(0)
                d = candidate.pop(0)
                cover = cur + d
                while traverse_list and traverse_list[0] <= cover: traverse_list.pop(0)
            
            if not traverse_list:
                return True

    return False
             

def solution(n, weak, dist):
    answer = 0
    wall = [0] * n
    dist = sorted(dist,reverse=True)

    # 몇명
    for i in range(1,len(dist)+1):
        # f 는 갈수 있는 길이의 모음
        f = list(permutations(dist,i))
        print(f)
        if ck(n,weak,i,f):
            print(i)
            return i
    return -1


# import sys
# import os

# def permutation(candidates, Prepermuation, res):
#     if len(candidates) == 0: res.append(Prepermuation); return
#     else:
#         for i in range(len(candidates)):
#             permutation(candidates[:i]+candidates[i+1:], Prepermuation + [ candidates[i] ], res)
#         return

# def solution(n, weak, dist):
#     # complete search
#     dist.sort(reverse = True)

#     for i in range(1, len(dist)+1):
#         permutations = []; permutation(dist[:i], [], permutations)
#         print(permutations)
#         for p in permutations:
#             for start in range(len(weak)):
#                 _left = weak[:start]; _right = weak[start:]
#                 traverse_list = _right + [x+n for x in _left];
#                 # print(p) 
#                 candidate = p.copy()
#                 print(candidate)
#                 while traverse_list and candidate:
#                     cur = traverse_list.pop(0); d = candidate.pop(0);
#                     print(d)
#                     Cover = cur + d
#                     while traverse_list and traverse_list[0] <= Cover: traverse_list.pop(0)

#                 if not traverse_list:
#                     return i
#     return -1
solution(50, [1, 5, 10, 12, 22, 25], [4, 3, 2, 1])