# '#': 벽, '.': 빈 공간
n = int(input())
x, y = map(int, input().split())
board = [list(''.join(input().split())) for _ in range(n)]

x -= 1
y -= 1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우 하 좌 상 (시계 방향)
time = 0 
direction = 0 # 우

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

def simulaton(x, y):
    global direction, time
    nx, ny = x + dxs[direction], y + dys[direction]

    # 1. 현재 방향으로 이동 불가
    if in_range(nx, ny) and board[nx][ny] == '#':
        # 반시계 방향으로 회전 
        direction = (direction -1) % 4

    # 2. 이동은 가능하나 격자 밖이라면 - 탈출
    elif not in_range(nx, ny):
        time += 1
        x, y = nx, ny
        return x, y

    # 3. 이동 가능하고 
    elif in_range(nx, ny) and board[nx][ny] == '.':
        # 3-1. 오른쪽(시계방향)에 짚을 벽이 있다면  
        rd = (direction + 1) % 4  # right direction
        rx, ry = nx + dxs[rd], ny + dys[rd]

        if board[rx][ry] == '#':
            # 그 뱡향으로 이동 
            time += 1
            x, y = nx, ny

            return x, y

        # 3-2. 오른쪽에 벽이 없다면 
        if board[rx][ry] == '.':
            # 현재 방향으로 한 칸 이동 
            time += 1
            # 회전 후 전진 
            time += 1 

            direction = rd
            x, y = rx, ry
            return x, y

    return x, y

while in_range(x, y):
    x, y = simulaton(x, y)
    # 길이 없을 경우 
    if time > n * n + n:
        time = -1
        break 

print(time)