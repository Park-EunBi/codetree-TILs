# 입력 - 0: 이동 가능, 1: 이동 불가 
from collections import deque 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
q = deque()
cnt = 0

def push(x, y):
    global cnt
    # 1. 큐 삽입 
    q.append((x, y))
    # 2. 방문 처리 
    visited[x][y] = 1
    # 3. 숫자 세기 
    cnt += 1

def canGo(x, y):
    # 1. 격자 외부 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 2. 방문 확인, 이동 가능 여부 확인 
    if visited[x][y] == 1 or board[x][y] == 1:
        return False 
    return True  

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                push(nx, ny)

# main
for _ in range(k): 
    cx, cy = map(int, input().split())
    q.append((cx - 1,cy - 1))
    bfs()

print(cnt)