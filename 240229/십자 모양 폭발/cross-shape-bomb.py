n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

temp_board = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
x-= 1
y-= 1
length = board[x][y]


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True


# 폭탄 터뜨리기 
board[x][y] = 0
for l in range(1, length):
    for dx, dy in zip(dxs, dys):
        nx = x + (dx * l)
        ny = y + (dy * l)
        
        if in_range(nx, ny):
            board[nx][ny] = 0

# 중력 
for j in range(n):
    idx = n - 1
    for i in range(n-1, -1, -1):
        if board[i][j]:
            temp_board[idx][j] = board[i][j]
            idx -= 1

for b in temp_board:
    print(*b)