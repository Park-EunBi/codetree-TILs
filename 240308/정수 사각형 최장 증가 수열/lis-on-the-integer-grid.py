n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[1 for _ in range(n)] for _ in range(n)]
cells = [] # 오름차순 정렬 한 값 
ans = 0
dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

# (칸에 적힌 값, x, y)
for i in range(n):
    for j in range(n):
        cells.append((board[i][j], i, j))

# 정렬 
cells.sort()

# 정수 값이 작은 순서대로 4방향에 대해 dp 갱신 
for _, x, y in cells:
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and board[nx][ny] > board[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

# 최댓값 찾기 
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)