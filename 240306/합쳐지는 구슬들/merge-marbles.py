n, m, t = map(int, input().split())
balls = [list(input().split()) for _ in range(m)]
count = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
direction ={
    'U':0,
    'R':1,
    'L':2,
    'D':3
}

# balls, count 전처리
for b in balls:
    b[0] = int(b[0]) - 1
    b[1] = int(b[1]) - 1
    b[2] = direction[b[2]]
    b[3] = int(b[3])
    count[b[0]][b[1]] += 1

###### fun
def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True 

# b에 입력된 방향대로 이동
def move(b):
    x, y, d, w = b
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny):
        return (nx, ny, d, w)
    else:
        return (x, y, 3 - d, w)

def simulation():
    global balls, count
    # 1. 구슬 이동 
    temp_balls = []
    for b in balls:
        temp_balls.append(move(b))
    balls = temp_balls

    # 2. count update
    temp_count = [[0 for _ in range(n)] for _ in range(n)]
    for b in balls:
        temp_count[b[0]][b[1]] += 1
    count = temp_count

    # 3. 충돌 처리 - 무게처리(방향 - 덮어쓰기, 무게 - 더하기), 제거 
    # count 돌다가 2 이상인 값 만나면 
    # balls 에서 x, y 같은 거 찾아서 wight, direction 갱신   
    for i in range(n):
        for j in range(n):
            # 충돌 감지
            nw = 0
            nd = -1 
            max_idx = -1
            if count[i][j] > 1:
                # 누군지 찾기 
                for idx, b in enumerate(balls):
                    if b[0] == i and b[1] == j:
                        nw += b[3]
                        nd = b[2]
                        max_idx = idx
                        # 지우기
                        balls[idx] = (-1, -1, -1, -1)
            
                count[i][j] = 1
                balls[max_idx] = (i, j, nd, nw)

    temp_balls = []
    for idx, b in enumerate(balls):
        if b == (-1, -1, -1, -1):
            continue
        else:
            temp_balls.append(b)

    balls = temp_balls


###### main
for _ in range(t):
    simulation()

cnt = sum([
    count[i][j]
    for i in range(n)
    for j in range(n)
])

weight = max([
    balls[i][3]
    for i in range(len(balls))
])

print(cnt, weight)