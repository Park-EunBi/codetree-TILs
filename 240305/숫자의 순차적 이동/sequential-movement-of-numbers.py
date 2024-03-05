n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

def move(x, y):
    # temp = [[0 for _ in range(n)] for _ in range(n)]
    max_num = 0
    max_pos = (0, 0)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and board[nx][ny] > max_num:
            max_num = board[nx][ny]
            max_pos = (nx, ny)

    # 교체 
    board[x][y], board[max_pos[0]][max_pos[1]] = board[max_pos[0]][max_pos[1]], board[x][y]

for _ in range(m):
    visited = [0 for _ in range(n * n + 1)]
    # 현재 확인 해야 하는 수 (1 ~ n * n)
    for cnt in range(1, n * n + 1):
        # 1. 확인해야 하는 수 위치 찾기 
        for i in range(n):
            for j in range(n):
                if board[i][j] == cnt and not visited[cnt]:
                    # 2. 이동 
                    move(i, j)
                    visited[cnt] = 1
                    
for b in board:
    print(*b)