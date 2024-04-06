from collections import deque
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 0: 빈칸
people = [list(map(int, input().split())) for _ in range(m)]
goal = list(map(int, input().split()))

# 상, 하, 좌, 우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# 인덱스 처리
for i in range(m):
    people[i][0] -= 1
    people[i][1] -= 1

goal[0] -= 1
goal[1] -= 1


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def bfs(q, visited):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and not board[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

# 한 명씩 최단 거리로 이동
def shortest(x, y, visited):
    global goal, ans

    # 1. 맨허튼 거리 계산
    dist = abs(x - goal[0]) + abs(y - goal[1])
    # print(f'x: {x}, y: {y}, dist:{dist}')

    # 2. 사방에 맨허튼 거리와 같은 거리인 곳 있는지 확인
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            # 상하 우선인지 반드시 확인 -> ok
            if visited[nx][ny] == dist:
                # 해당 좌표로 이동
                ans += 1
                return nx, ny

    # 최단 거리인 곳이 없음
    return x, y

def move():
    # 1. 동시 이동
    # temp = [[0 for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         temp[i][j] = board[i][j]
    temp = []

    # 2. 최단거리 계산
    q = deque()
    q.append(goal) # 거꾸로 돌릴 것임
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[goal[0]][goal[1]] = 1
    bfs(q, visited)

    # 3. 최단 거리로 이동
    for x, y in people:
        x, y = shortest(x, y, visited)
        # 도착 처리
        if (x, y) == (goal[0], goal[1]):
            continue
        else:
            temp.append([x, y])

    '''
    ###########디버깅 코드############
    print('<<temp>>')
    for t in temp:
        print(*t)
    print()
    print('<<visited>>')
    for v in visited:
        print(*v)
    print()
    # print('<<temp>>')
    # print(*temp)
    # print()
    #################################
    '''

    return temp

# 모든 사람에 대한 박스 만들기
def make_boxes():
    boxes = [] # (박스 시작 x, 박스 시작 y, 박스 길이)
    # 1. (x, y) ~ (goal) 작은 박스 만들기
    gx, gy = goal[0], goal[1]
    for x, y in people:
        d = max(abs(gx - x), abs(gy - y))

        if gx == x:
            for i in range(d, 0, -1):
                tx = gx - i
                if tx < 0:
                    continue
                else:
                    break


            # tx = gx - d
            # if tx < 0:
            #     tx = gx
            ty = min(gy, y)

        elif gy == y:
            ty = gy - d
            if ty < 0:
                ty = gy
            tx = min(gx, x)

        # if gx == x:
        #     tx = gx - d
        #     if tx < 0:
        #         tx = gx
        #     ty = min(gy, y)
        #
        # elif gy == y:
        #     ty = gy - d
        #     if ty < 0:
        #         ty = gy
        #     tx = min(gx, x)

        else:
            tx, ty = min(gx, x), min(gy, y)

        boxes.append((tx, ty, d))
        # print(f'박스: x: {tx}, y :{ty}, 길이: {d}')

    # 2. 박스 정렬하기
    boxes.sort(key = lambda x: (x[2], x[0], x[1]))

    return boxes[0][0], boxes[0][1], boxes[0][2]


def box_roate(x, y, d):
    global goal, people
    tx, ty, td = x, y, d # 내구도 감소에 사용
    # print(x, y, d)
    # 출구 회전에 사용
    board[goal[0]][goal[1]] = -1 # 출구
    # 사람 회전에 사용
    for px, py in people:
        board[px][py] = -100 # 사람


    # 0. 반복
    # for _ in range(d//2 + 1):
    for _ in range((td + 1)//2):
        for k in range(td):
            # 1. 왼 -> 오
            # print(k, 1)
            temp = board[x][y + d]
            for j in range(d, 0, -1):
                board[x][y + j] = board[x][y + j - 1]
            # for b in board:
            #     print(*b)
            # print()
            # 2. 하 -> 상
            # print(k, 2)
            for i in range(d):
                board[x + i][y] = board[x + i + 1][y]
            # for b in board:
            #     print(*b)
            # print()
            # 3. 우 -> 좌
            # print(k, 3)
            for j in range(d):
                board[x + d][y + j] = board[x+ d][y + j + 1]
            # for b in board:
            #     print(*b)
            # print()
            # 4. 상 -> 하
            # print(k, 4)
            for i in range(d, 0, -1):
                # print('here')
                board[x + i][y + d] = board[x + i - 1][y + d]
            board[x + 1][y + d] = temp



        x += 1
        y += 1
        d -= 2

    # 5. 출구, 사람 저장
    temp_people = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                goal = (i, j)
                board[i][j] = 0
            elif board[i][j] == -100:
                temp_people.append((i, j))
                board[i][j] = 0
    people = temp_people

    # 6. 내구도 감소
    for i in range(td + 1):
        for j in range(td + 1):
            if board[tx + i][ty + j]:
                board[tx + i][ty + j] -= 1


def rotate():
    # 1. 박스 만들기
    bx, by, length = make_boxes()
    # print(f'bx: {bx}, by: {by}, length: {length}')

    # 2. 회전
    ########## 경계만 회전인지, 전체 회전인지
    box_roate(bx, by, length)


end = False
ans = 0
# main
for _ in range(k):
    # 1. 이동
    people = move()

    # 종료 조건
    if not len(people):
        break

    # 2. 회전
    rotate()

print(ans)
print(goal[0] + 1, goal[1] + 1)