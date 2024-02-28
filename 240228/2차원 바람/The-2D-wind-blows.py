from copy import deepcopy
n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
boxes = [tuple(map(int, input().split())) for _ in range(q)]

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    return True

# 시계방향 회전 
def winds():  
    # 위쪽 이동 
    temp = board[r1][c2]
    board[r1].insert(c1, board[r1].pop(c2))

    # 왼쪽 이동 
    for r in range(r1, r2):
        board[r][c1] = board[r + 1][c1]
    
    # 아래쪽 이동 
    for c in range(c1, c2):
        board[r2][c] = board[r2][c + 1]
    
    # 오른쪽 이동 
    for r in range(r2, r1, -1):
        board[r][c2] = board[r - 1][c2]

    board[r1 + 1][c2] = temp 

# 값 갱신
def calc():
    # copy_board 내용으로 값을 계산하고 값을 board에 저장 
    # copy_board = deepcopy(board)
    copy_board = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy_board[i][j] = board[i][j]

    # 박스 안 탐색 
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):

            total = copy_board[x][y] # 주변 박스 값의 합 
            cnt = 1 # 주변 박스 개수 

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    cnt += 1
                    total += copy_board[nx][ny]
                    
            # 값 갱신 
            board[x][y] = total//cnt


for i in range(q):
    r1, c1, r2, c2 = boxes[i]

    # index 처리 
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    # 1. 회전 
    winds()

    # 2. 값 갱신 
    calc()

for b in board:
    print(*b)