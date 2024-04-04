n = int(input())
board= [list(map(int, input().split())) for _ in range(n)]

# 시작 위치 설정 
curr_x, curr_y = n//2, n//2
move_dir, move_num = 0, 1

ans = 0

dust_ratio = [
    [
        [0,  0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5,  0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0,  0, 2, 0, 0],
    ],
    [
        [0,  0, 0,  0, 0],
        [0,  1, 0,  1, 0],
        [2,  7, 0,  7, 2],
        [0, 10, 0, 10, 0],
        [0,  0, 5,  0, 0],
    ],
    [
        [0, 0, 2,  0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0,  0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2,  0, 0],
    ],
    [
        [0,  0, 5,  0, 0],
        [0, 10, 0, 10, 0],
        [2,  7, 0,  7, 2],
        [0,  1, 0,  1, 0],
        [0,  0, 0,  0, 0],
    ]
]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

# 먼지 추가 
def add_dust(x, y, dust):
    global ans 

    # 격자 범위를 벗어나면 답에 더하기 
    if not in_range(x, y):
        ans += dust
    else:
        board[x][y] += dust

def move():
    global curr_x, curr_y

    # 왼, 아, 오, 위
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]

    curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]

    # 각 위치에 먼지 더하기 
    added_dust = 0 # 총 이동한 먼지 
    for i in range(5):
        for j in range(5):
            dust = board[curr_x][curr_y] * dust_ratio[move_dir][i][j] // 100
            # ✨공부할 부분 
            # dust_ratio의 (0, 0) 부터 더해줘야 함 
            # 현재 위치를 (0, 0)으로 이동 시키고 (-2, -2)
            # range(5)를 돌며 모든 값을 더해준다  
            add_dust(curr_x + i - 2, curr_y + j -2, dust)

            added_dust += dust

    # a% 자리 
    # 내 위치에서 한 칸 앞으로 이동한 자리 (move_dir 방향으로)
    add_dust(curr_x + dxs[move_dir], curr_y + dys[move_dir], board[curr_x][curr_y] - added_dust)

# (0, 0) 확인
def end():
    if curr_x == 0 and curr_y == 0:
        return True
    return False 

# main 
while not end():
    # move_num 만큼 이동 
    for _ in range(move_num):
        move()

        # (0, 0)에 도착하면 종료
        if end():
            break

    
    # 이동 후 - 회오리 돌리기 
    move_dir = (move_dir + 1) % 4
    if move_dir == 0 or move_dir == 2:
        move_num += 1

print(ans)