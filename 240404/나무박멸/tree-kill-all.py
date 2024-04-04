# 0: 빈 칸, -1: 벽, 1 ~ 100 : 나무 수
n, m, k, c = map(int, input().split())  # 격자크기, 반복 수, 확산 범위, 제초제 지속 년 수
board = [list(map(int, input().split())) for _ in range(n)]
die = [[0 for _ in range(n)] for _ in range(n)]  # 제초제

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


def grow():
    # 0. 동시 성장
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    # print('<<grow_temp>>')
    # for t in temp:
    #     print(*t)
    # print()

    # 1. 인접 네 칸 중 나무가 있는 칸 만큼 성장
    for x in range(n):
        for y in range(n):
            cnt = 0  # 인접한 나무의 개수
            if 1 <= board[x][y] <= 100:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and 1 <= board[nx][ny] <= 100:
                        cnt += 1

            temp[x][y] += cnt

    return temp


def add():
    # board[x][y] == 0 이면 번식
    # 0. 동시 성장
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = board[i][j]

    # 1. 빈 칸의 개수 만큼 번식
    for x in range(n):
        for y in range(n):
            cnt = 0  # 빈 칸의 개수
            if 1 <= board[x][y] <= 100:
                # 번식 시작
                # 1-1. 빈 칸의 개수 세기 (빈 칸인 경우만)
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and not board[nx][ny] and not die[nx][ny]:
                        cnt += 1

                # 1-2. 번식할 나무의 수 계산
                if cnt != 0:
                    trees = board[x][y] // cnt

                # 1-3. 번식
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and not board[nx][ny] and not die[nx][ny]:
                        temp[nx][ny] += trees

    return temp


def use(x, y):

    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    temp_die = [[0 for _ in range(n)] for _ in range(n)]

    # 복사
    for i in range(n):
        for j in range(n):
            temp_board[i][j] = board[i][j]
            temp_die[i][j] = die[i][j]

    # 초기 위치 처리
    cnt = board[x][y]
    temp_board[x][y] = 0
    temp_die[x][y] = k  # 현재 위치 제초제 뿌리기

    # 대각선
    for dx, dy in zip([-1, -1, 1, 1], [-1, 1, -1, 1]):
        wall = False
        while not wall:
            for i in range(1, k + 1):  #### 주의 범위, dx, dy 순서 (wall flag 진짜 멈추는지)
                nx, ny = x + (dx * i), y + (dy * i)

                if in_range(nx, ny):
                    # print(f'nx: {nx}, ny:{ny}, i(퍼진 범위): {i}')
                    # 1. 나무라면
                    if 1 <= board[nx][ny] <= 100:
                        cnt += board[nx][ny]
                        temp_board[nx][ny] = 0
                        temp_die[nx][ny] = k

                    # 2. 벽이면 멈추기
                    if board[nx][ny] == -1:
                        # temp_die[nx][ny] = k
                        wall = True
                        break
                    # 3. 빈 공간이라면 멈추고제초제 뿌리기
                    if board[nx][ny] == 0:
                        temp_die[nx][ny] = k
                        wall = True
                        break
            wall = True


    return temp_board, temp_die, cnt


def spread():
    global board, die
    temp_board = [[0 for _ in range(n)] for _ in range(n)]
    temp_die = [[0 for _ in range(n)] for _ in range(n)]
    max_die = -1
    mx, my = -1, -1
    loc = [] # (죽은 나무 수, mx, my)

    # 1. 제초제를 뿌렸을 때 가장 많은 나무가 죽는 위치 구하기
    for i in range(n):
        for j in range(n):
            if 1 <= board[i][j] <= 100:
                _, _, temp = use(i, j)
                if max_die < temp:
                    max_die = temp
                    loc.append((max_die, i, j))

    loc.sort(key = lambda x: (-x[0], x[1], x[2]))


    board, die, die_trees = use(loc[0][1], loc[0][2])



    return board, die, die_trees  # 박멸한 나무 그루 수


def after(die):
    for a in range(n):
        for b in range(n):
            if die[a][b]:
                die[a][b] -= 1

    return die


# main
ans = 0
for i in range(m):

    # 1. 성장
    board = grow()

    # 2. 번식
    board = add()

    # 3. 제초
    if i > 0:
        die = after(die) # 제초제를 뿌리기 전 감소시킴
    board, die, die_trees = spread()
    ans += die_trees


print(ans)