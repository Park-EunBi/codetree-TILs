# 0: 이동 가능, 1: 이동 불가 
from collections import deque 
from itertools import combinations
from copy import deepcopy

n, k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

starts = []
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    starts.append((a, b))

# 돌의 위치 좌표화 
stones = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j]
]

# 제거할 돌의 조합 - 하나씩 돌아가면서 제거
removes = list(combinations(list(range(len(stones))), m))
maximum = -1
cnt = 0 # 이동 가능 위치 카운트 
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
q = deque()

def canGo(x, y, remove_board):
    # 1. 범위 확인 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 2. 이동 가능, 방문 여부 확인 
    if remove_board[x][y] or visited[x][y]:
        return False 
    return True

def push(x, y):
    # 1. push
    q.append((x, y))
    # 2. 방문 처리 
    visited[x][y] = 1

def bfs(remove_board):
    global cnt

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny, remove_board):
                push(nx, ny)
                cnt += 1

# 돌 치우기 
def remove_stones(i):
    # remove_board = board[:]
    remove_board = deepcopy(board)
    remove_list = removes[i]
    for j in remove_list:
        x, y = stones[j] # 제거할 돌의 위치 
        remove_board[x][y] = 0
    return remove_board

for i in range(len(removes)):
    # 돌 치우기 
    remove_board = remove_stones(i)
    # 모든 시작점 돌기 
    for x, y in starts:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        # cnt = 1
        cnt = 0
        q.append((x, y))
        bfs(remove_board)
        maximum = max(maximum, cnt)

print(maximum)