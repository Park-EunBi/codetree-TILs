# 0: 이동 가능, 1: 이동 불가 
n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]\

for i in range(n):
    for j in range(m):
        visited[i][j] = board[i][j]

visited[x][y] = 2

# 북, 동, 남, 서
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] 

can_go = True

def move():
    global d, x, y

    # 2. 좌회전 후 1번 반복 
    for _ in range(4):
        # 1. 현재 방향을 기준으로 왼쪽 방향 확인 
        d = (d-1) % 4
        nx, ny = x + dxs[d], y + dys[d]

        if not board[nx][ny] and not visited[nx][ny]:
            # 전진
            x, y = nx, ny
            visited[x][y] = 2
            return True

    return False 

while can_go:
    if not move():
        # 3. 4 방향 다 확인했는데도 전진 못함 -> 후진
        nd = (d + 2) % 4
        nx, ny = x + dxs[nd], y + dys[nd]
        
        # 4. 이동 못하면 종료
        if board[nx][ny]: 
            can_go = False 
        
        # 이동 가능하면 
        x, y = nx, ny

# 계산 
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 2:
            cnt += 1

print(cnt)