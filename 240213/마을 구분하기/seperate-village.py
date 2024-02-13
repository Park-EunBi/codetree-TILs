# 마을의 개수, 마을에 있는 사람 수 오름차순 출력 
# 1: 사람, 0: 벽

n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

country = []
cnt = 1
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def canGo(x, y):
    # 1. 격자 외부
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 2. 방문 여부, 장애물 확인 
    if board[x][y] == 0:
        return False 
    return True

def dfs(x, y):
    global cnt

    # 방문처리 
    board[x][y] = 0
    # cnt += 1
    # 인접 노드 방문
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if canGo(nx, ny):
            cnt += 1
            dfs(nx, ny)            
            return True

    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            country.append(cnt)
            cnt = 0

print(len(country))
for c in sorted(country):
    print(c)