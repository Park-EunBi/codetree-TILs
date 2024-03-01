n, r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
move = True 

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

def simulation(x, y):
    global move
    # 1. 현재 값 확인 
    now = board[x][y]
    # 2. 이동 
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and now < board[nx][ny]:
            return nx, ny
    move = False 
    return x, y

x = r - 1
y = c - 1

while move:
    print(board[x][y], end=' ')
    x, y = simulation(x, y)