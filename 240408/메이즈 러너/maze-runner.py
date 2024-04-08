# 0: 빈칸, -100: 벽, -1 ~ -10 : 사람 (누적 수)
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
people = [list(map(int, input().split())) for _ in range(m)]
goal = list(map(int, input().split()))

# idx 처리
for i in range(m):
    people[i] = [people[i][0] - 1, people[i][1] - 1]
goal = [goal[0] - 1, goal[1] - 1]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# 사방 확인 후 이동거리 줄어드는 방향으로
def move():
    global people, ans
    # 0. 동시 이동
    temp = [] # 사람 좌표
    gx, gy = goal[0], goal[1]

    # 1. 최단 거리 확인
    for x, y in people:
        # 최단 거리 확인
        dist = abs(gx - x) + abs(gy - y)
        # 사방 확인
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not board[nx][ny]:
                    if dist > abs(gx - nx) + abs(gy - ny):
                        temp.append((nx, ny))
                        ans += 1
                        break
        else:
            temp.append((x, y))

    # 출구 탈출
    people = temp[:]
    temp = []
    for x, y in people:
        if (x, y) != (gx, gy):
            temp.append((x, y))

    return temp


def find_box():
    # 가장 작은 한 변의 길이 찾기
    length = []
    gx, gy = goal[0], goal[1]
    people.sort(key= lambda x: (x[0], x[1]))

    for x, y in people:
        length.append(max(abs(gx - x), abs(gy - y)))

    length = length[0]

    # 완탐으로 사각형 찾기 (사람과 목적지를 포함한 길이가 length인 사각형)
    for x, y in people:
        for i in range(n - length):
            for j in range(n - length):
                # 사람 포함 확인
                if i <= x <= i + length and j <= y <= j + length:
                    # 목적지 포함 확인
                    if i <= gx <= i + length and j <= gy <= j + length:
                        return i, j, length


# 미로 회전, 내구도 감소
def turn(x, y, length):
    global people, goal

    # 1. 사람(-1), 목적지(-100) 복사
    for px, py in people:
        board[px][py] = -1
    board[goal[0]][goal[1]] = -100

    # 0. 동시 회전
    temp = [b[:] for b in board]

    # 2. 시계방향 90도 회전
    for i in range(0, length + 1):
        for j in range(0, length + 1):
            # print(i, j, length - j, i)
            board[i + x][j + y] = temp[length - j + x][i + y]
            # 내구도 감소
            if board[i + x][j + y] > 0:
                board[i + x][j + y] -= 1



    # 사람, 목적지 이동 처리
    people = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == -100:
                goal = [i, j]
                board[i][j] = 0
            elif board[i][j] < 0:
                people.append([i, j])
                board[i][j] = 0



def rotate():
    # 1. 가장 작은 정사각형 찾기
    x, y, length = find_box()

    # 2. 시계방향 90도 회전
    turn(x, y, length)



# main
for i in range(k):
    # 1. 이동
    people = move()

    # 2. 종료 조건 추가 - 사람 0 일 때
    if not len(people):
        break

    # 3. 회전
    rotate()

print(ans)
print(goal[0] + 1, goal[1] + 1)