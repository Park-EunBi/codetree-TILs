from collections import deque
n, m, k = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(n)]
board = [[[0, -1] for _ in range(m)] for _ in range(n)] # (공격력, 공격턴)

for i in range(n):
    for j in range(m):
        board[i][j][0] = temp[i][j]



# [1]. 공격자 선정 - 가장 약한
def find_attacker(time):
    mn = float('inf')

    # 1. 부셔지지 않은 포탑 중 가장 약한 포탑
    for i in range(n):
        for j in range(m):
            if board[i][j][0] > 0:
                # print(i, j)
                if board[i][j][0] < mn:
                    # print(f'공격력: {i, j, board[i][j][0]}')
                    mn = board[i][j][0]
                    temp = [(i, j, i + j, board[i][j][1])] # 공격력 작은 녀석들 등록 (x, y, ( x+ y), 최근 공격 시간)
                elif board[i][j][0] == mn:
                    temp.append((i, j, i + j, board[i][j][1]))


    # 1-2. 중복 정렬
    # (행, 열, 행+열, 공격 차수)
    temp.sort(reverse=True, key= lambda x: (x[3], x[2], x[1]))

    ax, ay = temp[0][0], temp[0][1]
    # print(f'공격자 좌표: {ax, ay}')
    # 2. 핸디캡 적용, 공격 턴 입력
    board[ax][ay][0] += (n + m)
    board[ax][ay][1] = time

    return ax, ay

# [2]. 피해자 선정 - 가장 강한 (공격자 제외)
def find_victim(ax, ay):
    mx = -float('inf')

    # 1. 부셔지지 않은 포탑 중 가장 강한
    for i in range(n):
        for j in range(m):
            # 공격자 제외
            if (i, j) == (ax, ay):
                continue

            if board[i][j][0] > 0:
                if board[i][j][0] > mx:
                    mx = board[i][j][0]
                    temp = [(i, j, i + j, board[i][j][1])]  # 공격력 큰 녀석들 등록 (x, y, (x+ y), 최근 공격 시간)
                elif board[i][j][0] == mx:
                    temp.append((i, j, i + j, board[i][j][1]))

    # 1-2. 중복 정렬
    # (행, 열, 행+열, 공격 차수)
    temp.sort(key=lambda x: (x[3], x[2], x[1]))
    # print('<<가장 강한 피해자 리스트 - 1명 선정 전, 정렬 완>>')
    # print(temp)
    vx, vy = temp[0][0], temp[0][1]
    # print(f'피해자 좌표: {vx, vy}')

    return vx, vy

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def bfs(ax, ay, vx, vy):
    # 고려할 것 - 우하좌상, 범위 초과시 넘어가기
    q = deque()
    q.append((ax, ay))
    # q.append((vx, vy))
    visited = [[() for _ in range(m)] for _ in range(n)]
    visited[ax][ay] = (ax, ay)
    # visited[vx][vy] = (vx, vy)
    vset.add((vx, vy))
    while q:
        x, y = q.popleft()
        # print(f'bfs: {x, y}')
        for dx, dy in zip((0, 1, 0, -1), (1, 0, -1, 0)):
        # for dx, dy in zip((-1, 0, 1, 0), (0, -1, 0, 1)):
            nx, ny = (x + dx) % n , (y + dy) % m
            # print(f'nx, ny : {nx, ny}')
            if visited[nx][ny] == () and board[nx][ny][0] > 0:
                q.append((nx, ny))
                visited[nx][ny] = (x, y)





    # 최단 경로 유무 판단
    if visited[vx][vy] == ():
        return False

    # 1. 레이저 공격
    # attack = board[ax][ay][0]
    # attack = board[vx][vy][0]
    attack = board[ax][ay][0]
    # ax, ay 에서 적힌 대로 따라가면 된다

    attack_q = deque()
    # attack_q.append((visited[ax][ay][0], visited[ax][ay][1]))
    # attack_q.append((visited[vx][vy][0], visited[vx][vy][1]))
    attack_q.append((vx, vy))

    # 2. 피해 입히기
    while attack_q:
        x, y = attack_q.popleft()

        vset.add((x, y))

        if (x, y) == (ax, ay):
            # return
            break

        if (x, y) == (vx, vy):
            # 공격력 만큼 공격
            board[x][y][0] = max(0, board[x][y][0] - attack)
            # print(attack)
            # continue # 확인 필요 ###########

        # 절반만큼 공격
        else:
            board[x][y][0] = max(0, board[x][y][0] - (attack//2))
        attack_q.append((visited[x][y][0], visited[x][y][1]))


    return True

# [2-1]. 레이저 공격
def razor(ax, ay, vx, vy):
    # 최단경로 거꾸로 - 그럼 우하좌상 우선순위는?
    # 고려할 것 - 우선순위 & 범위 초과시 넘어가기

    # 최단 경로 찾기 - 없으면 return False
    if bfs(ax, ay, vx, vy):
        return True
    return False

# [2-2]. 포탄 공격
def bomb(ax, ay, vx, vy):
    # 본인은 피해를 입지 않음 주의
    attack = board[ax][ay][0]
    # 1. 피해자 피해
    board[vx][vy][0] = max(0, board[vx][vy][0] - attack)
    vset.add((vx, vy))
    # 2. 주위 확산
    dxs, dys = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = (vx + dx) % n, (vy + dy) % m
        vset.add((nx, ny))
        # 공격자 제외
        if (nx, ny) == (ax, ay):
            continue
        # 공격
        board[nx][ny][0] = max(0, board[nx][ny][0] - attack//2)



# [3] 정비 - 관련 없는 것
def ready():
    for i in range(n):
        for j in range(m):
            if (i,j) not in vset and board[i][j][0] > 0:
                board[i][j][0] += 1





for time in range(k):

    vset = set() # 공격 받은 좌표 set


    # [1]. 공격자 선정 - 가장 약한
    ax, ay = find_attacker(time)
    vset.add((ax, ay)) # 공격자 자신 제외

    # [2]. 공격자 공격
    # [2-1]. 피해자 선정 - 가장 강한 (공격자 제외)
    vx, vy = find_victim(ax, ay)


    # [2-1]. 레이저 공격
    if not razor(ax, ay, vx, vy):
        # [2-2]. 포탄 공격
        bomb(ax, ay, vx, vy)




    # [종료 조건] 부셔지지 않은 포탑의 개수 -  얘 위치?
    count = sum([
        1
        for i in range(n)
        for j in range(m)
        if board[i][j][0] > 0
    ])


    if count <= 1:

        break

    # [3] 정비


    ready()


# 가장 강한 포탑 출력 (숫자만 비교하지 말고 조건 다 비교)

vx, vy = find_victim(-1, -1) # 모든 값 중 찾기
print(board[vx][vy][0])