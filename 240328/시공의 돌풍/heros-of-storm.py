# -1 : 돌풍 
n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
winds = []
ans = 0

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    return True

# 먼지 확산 
def spread():
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[i][j]
    
    for x in range(n):
        for y in range(m):
            if board[x][y] != -1: 
                fill = board[x][y] // 5
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and board[nx][ny] != -1:
                        # print(f'x:{x}, y:{y}, fill:{fill}, dx:{nx}, dy:{ny}')
                        temp[nx][ny] += fill
                        temp[x][y] -= fill
            # 돌풍 위치 기록 
            else: 
                winds.append((x, y))

    # print('<<<spread - board>>>')
    # for t in temp:
    #     print(*t)
    # print()

    return temp

def up(x, y, board):
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[i][j]
    
    # print(f'x: {x}, y: {y}')

    # 1. 왼쪽 
    for i in range(x, -1, -1):
        temp[i][0] = board[i-1][0]
    # 2. 위쪽 
    for j in range(0, m-1):
        temp[0][j] = board[0][j + 1]
    # 3. 오른쪽 
    for i in range(0, x):
        temp[i][m-1] = board[i+1][m-1]
    # 4. 아랫쪽
    for j in range(m-1, 0, -1):
        temp[x][j] = temp[x][j-1]

    # -1 위치 회복 
    temp[x][y] = -1
    # 돌풍에서 빠져 나온 바람 
    temp[x][1] = 0
    # print('<<<up-temp>>>')

    # for t in temp:
    #     print(*t)
    # print()

    return temp

def down(x, y, board):
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[i][j]
    
    # print(f'x: {x}, y: {y}')

    # 1. 왼쪽 
    for i in range(x, n-1):
        temp[i][0] = board[i+1][0]
    # 2. 위쪽 
    for j in range(m-1, 0, -1):
        temp[x][j] = temp[x][j-1]
    # 3. 오른쪽 
    for i in range(n-1, x, -1):
        temp[i][m-1] = board[i-1][m-1]
    # 4. 아랫쪽
    for j in range(0, m-1):
        temp[n-1][j] = board[n-1][j + 1]


    # -1 위치 회복 
    temp[x][y] = -1
    # 돌풍에서 빠져 나온 바람 
    temp[x][1] = 0
    # print('<<<down-temp>>>')

    # for t in temp:
    #     print(*t)
    # print()
    return temp


# 시계, 반시계 회전 
def wind():
    global board
    # print(winds)
    # 반시계 방향
    board = up(winds[0][0], winds[0][1], board) 
    
    # 시계 방향
    board = down(winds[1][0], winds[1][1], board)

def calc():
    total = sum(
        board[i][j]
        for i in range(n)
        for j in range(m)
        if board[i][j] != -1
    )

    return total 



# print('<<<init - board>>>')
# for b in board:
#     print(*b)
# print()

# main 
for _ in range(t):
    # a. 먼지 확산 
    board = spread()

    # b. 돌풍 
    wind()

    # c. 먼지 양 계산 
    ans = calc()

# print('ans: ', end ='')
print(ans)
# print('<<<board>>>')
# for b in board:
#     print(*b)