t = int(input())

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0] # U R L D
direction = {
    'U':0,
    'R':1,
    'L':2,
    'D':3
}

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

def move(x, y, d, temp_balls, temp_count):
    # 이동 
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny):
        temp_balls.append((nx, ny, d))
        temp_count[nx][ny] += 1
    # 방향 전환 
    else: 
        temp_balls.append((x, y, 3 - d))
        temp_count[x][y] += 1

def remove(x, y, d, temp_balls):
    global count

    # 해당 위치에 공이 2개인지 확인 
    if count[x][y] > 1:
        return 
    else:
        temp_balls.append((x, y, d))

def simulation():
    global balls, count

    temp_balls = []
    temp_count = [[0 for _ in range(n)] for _ in range(n)]

    # 1. 공 이동 
    for b in balls:
        move(b[0], b[1], b[2], temp_balls, temp_count)
    
    balls = temp_balls
    count = temp_count

    # 2. 충돌된 공 제거 - balls 
    temp_balls = []
    for b in balls:
        remove(b[0], b[1], b[2], temp_balls)
    
    balls = temp_balls

    # 3. 충돌된 공 제거 - count
    for i in range(n):
        for j in range(n):
            if count[i][j] > 1:
                count[i][j] = 0

for _ in range(t):
    n, m = map(int, input().split())
    balls = [list(input().split()) for _ in range(m)]
    count = [[0 for _ in range(n)] for _ in range(n)]

    for b in balls:
        b[0] = int(b[0]) - 1
        b[1] = int(b[1]) - 1
        b[2] = direction[b[2]]

        count[b[0]][b[1]] = 1

    for i in range(2 * n):
        simulation()

    ans = sum([
        count[i][j]
        for i in range(n)
        for j in range(n)
    ])

    print(ans)