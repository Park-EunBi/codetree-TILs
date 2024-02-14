# 탈출 가능한 경로가 있는지 판단
# 입력 - 1: 이동 가능, 0: 이동 불가 
# 출력 - 1: 탈출 가능, 0: 탈출 불가 
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()

def canGo(x, y):
    # 1. 범위 체크 
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    # 2. 방문 여부, 이동 가능 여부 확인 
    if board[x][y] == 0:
        return False 
    return True

def push(x, y):
    q.append((x, y))

def bfs():
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        board[x][y] = 0 # 방문 처리 
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                push(nx, ny)

push(0, 0)
bfs()

print(1 - board[n-1][m-1]) # 0 <-> 1 반전