from collections import deque
	

def move(f, s, new_board):
	dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
	temp = []
	 # 이동
	for i in range(4):
		y1, x1 = f[0] + dy[i], f[1] + dx[i]
		y2, x2 = s[0] + dy[i], s[1] + dx[i]

		if new_board[y1][x1] == 0 and new_board[y2][x2] == 0:
			temp.append([(y1, x1), (y2, x2)])

    # 회전
	d = [1, -1]
    # 가로
	if f[0] == s[0]:
		for r in d:
			if new_board[f[0] + r][f[1]] == 0 and new_board[f[0] + r][s[1]] == 0:
				temp.append(sorted([(f[0] + r, f[1]), (f[0], f[1])]))
				temp.append(sorted([(s[0] + r, s[1]), (s[0], s[1])]))
    # 세로
	else:
		for r in d:
			if new_board[f[0]][f[1] + r] == 0 and new_board[s[0]][s[1] + r] == 0:
				temp.append(sorted([(f[0], f[1]), (f[0], f[1] + r)]))
				temp.append(sorted([(s[0], s[1]), (s[0], s[1] + r)]))

	return temp


def solution(board):
	n = len(board)
	new_board = [[1] * (n + 2) for i in range(n + 2)]
    
	for i in range(len(board)):
		for j in range(len(board)):
			new_board[i + 1][j + 1] = board[i][j]

	dq = deque([[([1, 1], [1, 2]), 0]])
	visited = []

	while dq:
		now = dq.popleft()
		f, s = now[0]
		dist = now[1]
		if now[0] not in visited:
			visited.append(now[0])
		for i in move(f, s, new_board):
			if (n, n) in i:
				return dist + 1
			if i not in visited:
				visited.append(i)
				dq.append([i, dist + 1])
	return



# from collections import deque

# #1초동안 움직일 수 있는 모든 경우
# def move(cor1,cor2,board):
# 	move = [(1,0), (0,1), (-1,0), (0,-1)]
# 	ret=[]
# 	#이동
# 	for m in move:
# 		if board[cor1[0]+m[0]][cor1[1]+m[1]]==0 and board[cor2[0]+m[0]][cor2[1]+m[1]]==0:
# 			ret.append({(cor1[0]+m[0],cor1[1]+m[1]),(cor2[0]+m[0],cor2[1]+m[1])})

# 	rotate=[1,-1]
# 	#가로회전
# 	if cor1[0]==cor2[0]:
# 		for r in rotate:
# 			if board[cor1[0]+r][cor1[1]]==0 and board[cor2[0]+r][cor2[1]]==0:
# 				ret.append({(cor1[0]+r,cor1[1]),(cor1[0],cor1[1])})
# 				ret.append({(cor2[0]+r,cor2[1]),(cor2[0],cor2[1])})
# 	#세로회전
# 	else:
# 		for r in rotate:
# 			if board[cor1[0]][cor1[1]+r]==0 and board[cor2[0]][cor2[1]+r]==0:
# 				ret.append({(cor1[0],cor1[1]),(cor1[0],cor1[1]+r)})
# 				ret.append({(cor2[0],cor2[1]),(cor2[0],cor2[1]+r)})
# 	return ret

# def solution(board):
# 	size = len(board)
# 	#경계 체크 쉽게하기 위해서 지도의 상하좌우에 1 추가
# 	new_board = [[1 for i in range(len(board)+2)] for i in range(len(board)+2)]
# 	for i in range(len(board)):
# 		for j in range(len(board)):
# 			new_board[i+1][j+1] = board[i][j]

# 	que = deque()
# 	visited = []

# 	#queue에 [로봇의 좌표정보, 지금까지 거리] 형태로 넣음
# 	que.append([{(1,1),(1,2)},0])
# 	visited.append({(1,1),(1,2)})

# 	while len(que)!=0:
# 		temp = que.popleft()
# 		cor = list(temp[0])
# 		dist = temp[1]+1

# 		for m in move(cor[0],cor[1],new_board):
# 			if (size,size) in m: return dist

# 			if not m in visited:
# 				que.append([m,dist])
# 				visited.append(m)

# 	return 0

print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)
