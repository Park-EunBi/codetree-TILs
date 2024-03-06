n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
board = [[[int(x)] for x in input().split()] for _ in range(n)]
nums = list(map(int, input().split()))

dxs, dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# num의 위치 찾기 
def find_move(num):
    for i in range(n):
        for j in range(n):
            if num in board[i][j]:
                return i, j, board[i][j].index(num)

# x, y 위치에서 8 방향으로 인접 수 중 가장 큰 수 위치 반환 
def find_big(x, y):
    max_num = -1
    max_idx = (-1, -1)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            for check_num in board[nx][ny]:
                if check_num > max_num:
                    max_num = check_num
                    max_idx = (nx, ny)
    
    # 이동할 수 없을 경우 처리
    if max_idx == (-1, -1):
        return (x, y)
    else:
        return max_idx


def move(num):
    temp = []
    # 1. 움직일 숫자의 위치 찾기 
    x, y, idx = find_move(num)

    # 2. 이동시킬 덩이 빼기 
    temp = board[x][y][:idx + 1]
    board[x][y] = board[x][y][idx + 1:]

    # 3. 가장 큰 수 위치 찾기 
    bx, by = find_big(x, y)

    # # 4. 이동
    board[bx][by] = temp + board[bx][by]  

# main 
for num in nums:
    move(num)

# 출력 
for boa in board:
    for bo in boa:
        if bo:
            print(*bo)
        else:
            print('None')