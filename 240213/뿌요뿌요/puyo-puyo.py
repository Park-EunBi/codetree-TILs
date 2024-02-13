# 블럭을 이루는 칸의 수가 4개 이상이면 터짐 
# 터지게 되는 블럭 수, 최대 블럭의 크기 
# 방문처리: 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 0
ret = []
maximum = -1

def canGo(x, y, num):
    # 1. 격자 외부 
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    # 2. 다른 블럭인지 
    if board[x][y] != num:
        return False 
    # 3. 방문 한 곳인지 
    if board[x][y] == 0:
        return False 
    return True 

def dfs(x, y, num):
    global cnt
    # 방문 처리 
    board[x][y] = 0
    # 인접 노드 방문 
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if canGo(nx, ny, num):      
            dfs(nx, ny, num)
            cnt += 1

for i in range(n):
    for j in range(n):
        num = board[i][j]
        cnt = 1
        if canGo(i, j, num):
            if board[i][j] != 0:               
                dfs(i, j, num)
                maximum = max(maximum, cnt)
                if cnt >= 4:
                    ret.append(cnt)


print(len(ret), maximum)