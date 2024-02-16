from collections import deque
n = int(input())
sx, sy, ex, ey = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [1, 2, 1, 2, -1, -2, -1, -2], [2, 1, -2, -1, 2, 1, -2, -1]
q = deque()

def canGo(x, y):
    # 1. 범위 확인 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 2. 방문 확인
    if board[x][y]:
        return False 
    return True

def push(x, y, s):
    # 1. 추가 
    q.append((x, y))
    # 2. 방문 처리
    board[x][y] = s 

def bfs():
    while q:
        x, y = q.popleft()
        # 인접노드 방문 
        # print(board)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                push(nx, ny, board[x][y] + 1)

sx -= 1
sy -= 1

q.append((sx, sy))
board[sx][sy] = 1
bfs()

# 이동불가시 -1 출력 
print(board[ex-1][ey-1] - 1) if board[ex-1][ey-1] else print(-1)

'''
1
1 1 1 1

0
'''