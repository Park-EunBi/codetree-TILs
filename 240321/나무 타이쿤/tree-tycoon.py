n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]

# 영양제 위치 (1: 있음, 0: 없음)
pills = [[0] * n for _ in range(n)]
pills[n-1][0] = pills[n-1][1] = pills[n-2][0] = pills[n-2][1] = 1

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True 

def move_pills(d, p):
    # 이동한 것 temp에 저장 
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if pills[i][j]:
                x = (i + (dxs[d] * p)) % n
                y = (j + (dys[d] * p)) % n

                temp[x][y] = 1

    for i in range(n):
        for j in range(n):
            pills[i][j] = temp[i][j]   

# 영양제 주입
def inject():
    for i in range(n):
        for j in range(n):
            if pills[i][j]:
                board[i][j] += 1

# 대각선 확인 및 성장 
def check_diagonal():
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    # 1. 영양제 있는 땅 확인 
    for i in range(n):
        for j in range(n):
            if pills[i][j]:
                cnt = 0 # 리브로수 개수 세기 
                # 2. 대각선 방향 확인 
                for dx, dy in zip([-1, -1, 1, 1], [-1, 1, -1, 1]):
                    nx = i + dx
                    ny = j + dy
                    if in_range(nx, ny):
                        # 3. 높이 1 이상의 리브로수 개수 세기 
                        if board[nx][ny] >= 1:
                            cnt += 1
                
                temp[i][j] += cnt
    
    for i in range(n):
        for j in range(n):
            board[i][j] = temp[i][j]

# 베어내고, 영양제 올려두기 
def replace_pills():
    # 새 영양제 위치 
    temp= [[0] * n for _ in range(n)] 

    for i in range(n):
        for j in range(n):
            if not pills[i][j] and board[i][j] >= 2:
                board[i][j] -= 2
                temp[i][j] = 1

    for i in range(n):
        for j in range(n):
            pills[i][j] = temp[i][j]


# main 
for M in range(m):
    d, p = map(int, input().split()) # 방향, 칸
    d -= 1

    # 1. 영양제 이동 
    move_pills(d, p)

    # 2. 땅 속에 영양제 투입 
    inject()

    # 3. 대각선 확인 후 성장 
    check_diagonal()

    # 4. 베어내고, 영양제 올려두기 
    replace_pills()

ans = 0

ans = sum(
    board[i][j]
    for i in range(n)
    for j in range(n)
)

print(ans)