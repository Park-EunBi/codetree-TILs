# 1: 이동 가능, 0: 이동 불가 
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def canGo(x, y):
    # 1. 범위 확인 
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    # 2. 이동 가능 여부, 방문 여부 확인 
    if not board[x][y] or visited[x][y]:
        return False 
    return True

def push(x, y, s):
    # 1. 추가 
    q.append((x, y))
    # 2. 방문 처리 
    visited[x][y] = 1
    # 3. 이동 거리 갱신 
    board[x][y] = s

def bfs():
    while q:
        x, y = q.popleft()
        # 인접 노드 탐색 
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                push(nx, ny, board[x][y] + 1)


# 이동 불가시 -1 
q.append((0, 0))
board[0][0] = 0
bfs()

print(board[n-1][m-1]) if board[n-1][m-1] else print(-1)