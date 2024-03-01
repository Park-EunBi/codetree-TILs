n, m, r, c = map(int, input().split())
x = r - 1
y = c - 1
directions = input().split()
board = [[0 for _ in range(n)] for _ in range(n)]

dir_mapper = {
    'R': 0,
    'L': 1,
    'U': 2,
    'D': 3
}

# 주사위의 front, right, up 숫자를 정해주면 된다 
up, front, right = 1, 2, 3

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

# 이동했을 때의 다음 위치
def next_pos(x, y, move_dir):
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    return (nx, ny) if in_range(nx, ny) else (-1, -1)
    
def simulation(direction):
    global x, y
    global up, front, right

    nx, ny = next_pos(x, y, direction) 

    if (nx, ny) == (-1, -1):
        return 

    x, y = nx, ny

    # 주사위 상태 조정 
    if direction == 0: # 동쪽
        up, front, right = 7 - right, front, up
    elif direction == 1: # 서쪽
        up, front, right = right, front, 7 - up
    elif direction == 2: # 북쪽
        up, front, right = front, 7 - up, right
    else: # 남쪽
        up, front, right = 7 - front, up, right


    # 바닥 숫자 변경 
    bottom = 7 - up
    board[x][y] = bottom
    
# 초기 위치 저장 
board[x][y] = 6

for direction in directions:
    simulation(dir_mapper[direction])

ans = sum([
    board[i][j]
    for i in range(n)
    for j in range(n)
])

print(ans)