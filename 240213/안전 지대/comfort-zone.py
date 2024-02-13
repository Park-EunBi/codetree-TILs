n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0
safe = [-1, -1] # k, 안전 지역 개수 
def canGo(x, y):
    # 1. 범위 밖 
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    # 2. 안전 지대 확인 
    if board[x][y] <= k:
        return False 
    # 3. 방문 확인 
    if visited[x][y] == 1:
        return False

    return True 


def dfs(x, y):
    # 방문 처리 
    visited[x][y] = 1
    # 인접 노드 순회
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if canGo(nx, ny):
            dfs(nx, ny)


for k in range(1, 101):
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if canGo(i, j):
                visited[i][j] = 1
                # cnt += 1
                dfs(i, j)
                cnt += 1
    if safe[1] < cnt:
        safe = [k, cnt]
    cnt = 0

print(*safe)