n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r -= 1
c -= 1

# -, ↑, ↗, →, ↘, ↓, ↙, ←, ↖
# dire = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]\
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]
ans = -1 

def canGo(x, y, prev_num):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    if board[x][y] <= prev_num:
        return False 
    return True

# 어떤 칸으로 움직일지 선택 (현재보다 큰 칸으로만 이동)
def find_max(x, y, cnt):
    global ans

    ans = max(ans, cnt)

    d = directions[x][y] - 1 # 방향 설정 

    for i in range(n):
        nx, ny = x + dxs[d] * i, y + dys[d] * i
        if canGo(nx, ny, board[x][y]):
            find_max(nx, ny, cnt + 1)

find_max(r, c, 0)
print(ans)