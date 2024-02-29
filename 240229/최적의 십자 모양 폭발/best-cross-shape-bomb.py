n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = -float('inf')

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def copy():
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]
    return temp

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

def bomb(x, y, board):
    length = board[x][y]
    board[x][y] = 0

    for l in range(1, length):
        for dx, dy in zip(dxs, dys):
            nx = x + (dx * l)
            ny = y + (dy * l)
            if in_range(nx, ny):
                board[nx][ny] = 0

    return board

def down(board):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        idx = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j]:
                temp[idx][j] = board[i][j]
                idx -= 1

    return temp


def find(board):
    cnt = 0

    # 행 검사 
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] and board[i][j] == board[i][j + 1]:
                cnt += 1
    
    # 열 검사 
    for j in range(n):
        for i in range(n - 1):
            if board[i][j] and board[i][j] == board[i + 1][j]:
                cnt += 1

    return cnt


# 1. 모든 격자 돌기 
for i in range(n):
    for j in range(n):
        # 2. board 복사 
        copy_board = copy()
        # 3. 폭탄 
        copy_board = bomb(i, j, copy_board)
        # 4. 중력 
        copy_board = down(copy_board)
        # 5. 쌍 계산, 최댓값 갱신 
        ans = max(ans, find(copy_board))

print(ans)