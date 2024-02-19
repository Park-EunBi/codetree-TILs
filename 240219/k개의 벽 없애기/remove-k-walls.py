# 0: 이동 가능, 1: 이동 불가 
from collections import deque
import sys 
from copy import deepcopy
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
walls = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j] == 1
]

visited = [[0 for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

sx -= 1
sy -= 1
ex -= 1
ey -= 1

q = deque()

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
minimum = float('inf')

def remove_walls(remove):
    for r in remove:
        x, y = walls[r]
        board[x][y] = 0

def replace_walls(remove):
    for r in remove:
        x, y = walls[r]
        board[x][y] = 1

def canGo(x, y):
    # 1. 범위 확인 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 방문 여부, 이동 가능 여부 확인 
    if visited[x][y] or board[x][y]:
        return False 
    return True

def push(x, y, s):
    q.append((x, y))
    visited[x][y] = 1
    step[x][y] = s

def bfs():
    while q:
        x, y = q.popleft()
        # 인접 노드 방문 
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                push(nx, ny, step[x][y] + 1)
    
    if visited[ex][ey]:
        return step[ex][ey]
    else:
        return float('inf')

# 제거할 벽 선택 
remove = []
def choice(num):
    global minimum
    if len(remove) == k:
        remove_walls(remove)
        # step = [[0 for _ in range(n)] for _ in range(n)]
        # visited = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                visited[i][j] = 0
                step[i][j] = 0

        q.append((sx, sy))
        visited[sx][sy] = 1
        step[sx][sy] = 0
        minimum = min(minimum, bfs())
        replace_walls(remove)

        return 
    
    for i in range(num, len(walls)):
        if i not in remove:
            remove.append(i)
            choice(i + 1)
            remove.pop()

choice(0)

if minimum == float('inf'):
    print(-1)
else:
    print(minimum)