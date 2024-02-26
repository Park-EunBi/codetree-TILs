n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

block = [
    [(1, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (0, 1)],\
    [(0, 0), (1, 0), (2, 0)], [(0, 0), (0, 1), (0, 2)]
    ]
ans = -float('inf')

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    return True

def calc(x, y):
    cal = 0

    for b in block:
        ax, ay = b[0]
        bx, by = b[1]
        cx, cy = b[2]

        # 좌표 갱신 주의 
        if in_range(x + ax, y + ay) and in_range(x + bx, y + by) and in_range(x + cx, y + cy):
            cal = max(cal, board[x + ax][y + ay] + board[x + bx][y + by] + board[x + cx][y + cy])
        
    return cal

for i in range(n):
    for j in range(m): # 범위 주의
        ans = max(ans, calc(i, j))

print(ans)