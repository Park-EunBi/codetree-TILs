from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 시계 방향 (우, 하, 좌, 상)
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 벽 만나면 튕기기
def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >=n:
        return False
    return True

# 바닥면 찾기
def find_down(d):
    global up, front, right
    if d == 0:
        up, front, right = abs(7 - right), front, up
    elif d == 1:
        up, front, right = abs(7 - front), up, right
    elif d == 2:
        up, front, right = right, front, abs(7 - up)
    else:
        up, front, right = front, abs(7-up), right

    return abs(7-up)

# 주사위 이동 후 바닥면 숫자 반환
def move():
    global d, x, y
    # 1. d 방향 대로 이동 (x, y 갱신, 벽에 닿으면 튕기기)
    nx, ny = x + dxs[d], y + dys[d]
    if not in_range(nx, ny):
        d = (d + 2) % 4 # 튕기기
        x, y = x + dxs[d], y + dys[d]
    else:
        x, y = nx, ny

    # 2. 바닥면 판단 후 반환
    down = find_down(d)

    return down

def bfs(x, y, q, visited):
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

# 바닥면을 기준으로 상하좌우 모두 확인, 값 계산 - bfs 돌려야 함
def calc():
    global x, y

    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    cnt = bfs(x, y, q, visited)

    return board[x][y] * cnt

# 바닥면과 board를 비교하여 방향 전환
def change_dir(d):
    global down, x, y
    if board[x][y] < down:
        # 시계 방향
        d = (d + 1) % 4
    elif board[x][y] > down:
        # 반시계
        d = (d - 1) % 4
    return d

# main
ans = 0
x, y = 0, 0
d = 0
up, front, right = 1, 2, 3
for _ in range(m):
    # 1. 이동
    down = move()

    # 2. 계산
    ans += calc()

    # 3. 방향 전환
    d = change_dir(d)

print(ans)