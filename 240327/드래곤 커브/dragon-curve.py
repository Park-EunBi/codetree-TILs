# 회전 중심을 기준으로 드래콘 커브에 속하는 점들만 추가하며 관리 
# 회전 중심은 이전 중심을 시계방향으로 90도 회전하면 나옴 
GRID = 100
n = int(input())

# 현재 드래곤 커브를 이루고 있는 점들의 위치 
dragon_point = [
    [False for _ in range(GRID + 1)]
    for _ in range(GRID + 1)
]

# 새롭게 그려지는 드래콘 커브 점들의 위치 
new_dragon_point = [
    [False for _ in range(GRID + 1)]
    for _ in range(GRID + 1)
]

# 최종 드래곤 커브
paper = [
    [False for _ in range(GRID + 1)]
    for _ in range(GRID + 1)
]

# (x, y)를 (cx, cy) 기준으로 회전 
# 원점 이동 -> 회전 -> 기준점으로 평행 이동 
def rotate(x, y, cx, cy):
    # 1. 초기 좌표: (x, y), (cx, cy)
    # 2. 원점 이동: (x - cx, y - cy), (0, 0)
    # 3. 회전: (y - cy, cx - x), (0, 0)
    # 4, 평행 이동: (y - cy + cx, cx - x + cy), (cx, cy)
    return (y - cy + cx, cx - x + cy)

# 드래곤 커브 확장 
def simutation(cx, cy):
    # 초기화 
    for i in range(GRID + 1):
        for j in range(GRID + 1):
            new_dragon_point[i][j] = False

    # 새로운 드래곤 커브 그리기 
    for i in range(GRID + 1):
        for j in range(GRID + 1):
            if dragon_point[i][j]:
                # 기존 값 가져와서 cx, cy 기준으로 회전
                nx, ny = rotate(i, j, cx, cy)
                new_dragon_point[nx][ny] = True
    
    # 새로운 포인트를 현재 포인트에 추가 
    for i in range(GRID + 1):
        for j in range(GRID + 1):
            if new_dragon_point[i][j]:
                dragon_point[i][j] = True

def draw(x, y, d, g):
    # 초기화 
    for i in range(GRID + 1):
        for j in range(GRID + 1):
            dragon_point[i][j] = False
    
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

    # 0차 드래곤 커브 
    sx, sy = x, y
    ex, ey = x + dxs[d], y + dys[d]

    dragon_point[sx][sy] = True
    dragon_point[ex][ey] = True

    # 드래곤 커브 확장 
    for _ in range(g):
        simutation(ex, ey)

        # 마지막 위치 갱신 
        ex, ey = rotate(sx, sy, ex, ey)

    # 확장한 커브를 paper에 표시 
    for i in range(GRID):
        for j in range(GRID):
            if dragon_point[i][j]:
                paper[i][j] = True


# main 
for _ in range(n):
    x, y, d, g = tuple(map(int, input().split()))
    draw(x, y, d, g)

ans = sum([
    1
    for i in range(GRID)
    for j in range(GRID)
    if paper[i][j] and paper[i][j + 1]
    and paper[i + 1][j] and paper[i + 1][j + 1]
])

print(ans)