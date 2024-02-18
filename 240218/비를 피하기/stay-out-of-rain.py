# 0: 이동 가능, 1: 벽, 2: 사람 있음 (이동 가능), 3: 비 피하는 공간 (목적지)
from collections import deque 
import sys 
input = sys.stdin.readline

n, h, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ret = [[float('inf') for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
q = deque()

people = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j] == 2
]

goals = [
        (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j] == 3
]

def canGo(x, y):
    # 1. 범위 체크 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 

    # 2. 이동 가능 여부, 방문 여부
    if board[x][y] == 1 or visited[x][y]:
        return False 
    return True 

def push(x, y, s):
    # 1. 추가 
    q.append((x, y))
    # 2. 방문 처리, 이동 거리 체크
    visited[x][y] = s 
    

def bfs():
    global gx, gy, cnt
    while q:
        x, y = q.popleft()

        # bfs에서 탈출 조건 잡으면 최단 경로를 찾을 수 없다 
        # 모든 가능한 경로를 탐색하며 최단 거리를 계산하는 것이기 때문 
        # 처음으로 목적지에 도달한다고 해서 최단 거리임을 보장하지 않는다 

        # 인접 노드 방문 
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny):
                push(nx, ny, visited[x][y] + 1)

# sol_2: m개의 목적지를 시작으로 하는 bfs를 한 번 돌리면 된다 
# 목적지 부터 모든 지점까지의 최소 값을 찾을 수 있다 

# 모든 목적지를 큐에 넣는다 
for x, y in goals:
    push(x, y, 0)

bfs()


for i in range(n):
    for j in range(n):
        if board[i][j] != 2: # 사람이 서 있던 곳이 아니라면 
            print(0, end = ' ')
        else: # 사람이 서 있던 곳이라면 
            if not visited[i][j]: # 방문한 적이 없다면 
                print(-1, end = ' ') # 방문할 수 없는 것 
            else: # 방문 한 적 있다면 
                print(visited[i][j], end = ' ') # 최단 거리 출력 
    print()


'''
# 시간 초과
# sol_1: 모든 사람에 대해 모든 목적지의 최소 거리를 구한다 
for px, py in people:
    for gx, gy in goals:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        q.append((px, py))
        visited[px][py] = 1
        bfs()

        if visited[gx][gy]:
            ret[px][py] = min(ret[px][py], visited[gx][gy] - 1)
    if ret[px][py] == float('inf'):
        ret[px][py] = -1

for r in ret:
    for idx, i in enumerate(r):
        if i == float('inf'):
            r[idx] = 0

for r in ret:
    print(*r)
'''