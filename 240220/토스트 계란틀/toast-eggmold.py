from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
q = deque()

ans = 0
append_list = []  # 값 바꾸기 위해 좌표 등록
total = 0  # 분리한 판의 계란 수
cnt = 0  # 분리한 판 수

def canGo(x, y):
    # 1. 범위 확인
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
        # 이동 확인, 방문 확인
    if visited[x][y]:
        return False
    return True

def push(x, y):
    global total, cnt
    # 1. 추가
    q.append((x, y))
    # 2. 방문 처리
    visited[x][y] = 1
    # 3. 계산 데이터 등록
    total += board[x][y]
    cnt += 1
    append_list.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny) and (l <= abs(board[nx][ny] - board[x][y]) <= r):
                push(nx, ny)

    change = total // cnt
    for x, y in append_list:
        board[x][y] = change

while 1:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if canGo(i, j):
                # 값 추가
                push(i, j)
                visited[i][j] = 1
                bfs()
                count += 1

                # 초기화
                append_list = []  # 값 바꾸기 위해 좌표 등록
                total = 0  # 분리한 판의 계란 수
                cnt = 0  # 분리한 판 수

    if count == n * n:
        print(ans)
        break

    ans += 1