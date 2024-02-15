# bfs 로 이동 가능한 범위를 탐색한 뒤 그 중 숫자, 행, 열 순으로 정렬하여 값을 찾으면 된다 
from collections import deque
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split())
q = deque()

x -= 1
y -= 1
loc = [] 
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
# ret_x, ret_y = -1, -1

def canGo(x, y, check):
    # 1. 범위 확인 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 2. 방문 여부, 이동 가능 여부 
    if visited[x][y] == 1 or board[x][y] >= check:
        return False 
    return True

def push(x, y):
    # 1. 추가 
    q.append((x, y))
    # 2. 방문 처리 
    visited[x][y] = 1
    # 3. 이동 가능한 위치 저장
    loc.append((board[x][y], x, y)) # 값, 행, 열 

def bfs(check):
    while q:
    # 노드 뽑기 
        x, y = q.popleft()
        
        # 인접 노드 이동 
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny, check):
                push(nx, ny)



for _ in range(k):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q.append((x, y))
    visited[x][y] = 1
    loc = []
    bfs(board[x][y])
    # print(sorted(loc))
    # 위치 이동 - 최댓값 찾기 
    loc.sort(reverse = True, key = lambda x:(x[0], -x[1], -x[2]))
    x, y = (loc[0])[1], (loc[0])[2]


print(x + 1, y + 1)