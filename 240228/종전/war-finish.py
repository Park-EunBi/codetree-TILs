n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
numbers = [[0 for _ in range(n)] for _ in range(n)]
ans = float('inf')

def draw():
    # 1 번 구역 경계 표시
    for delta in range(w + 1):
        # 상 -> 좌
        numbers[i + delta][j - delta] = 1
        # 우 -> 하
        numbers[i + h + delta][j + h - delta] = 1
    for delta in range(1, h):
        # 상 -> 우
        numbers[i + delta][j + delta] = 1
        # 좌 -> 하
        numbers[i + w + delta][j - w + delta] = 1
    
    # 직선 경계 표시 
    for x in range(i):
        numbers[x][j] = 2
    for y in range(j + h + 1, n):
        numbers[i + h][y] = 3
    for y in range(j - w):
        numbers[i + w][y] = 4
    for x in range(i + w + h + 1, n):
        numbers[x][j - w + h] = 5

    # 2번 채우기 
    for x in range(i + w):
        for y in range(j):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 2

    # 3번 채우기 
    for x in range(i + h):
        for y in range(n - 1, j, -1):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 3 

    # 4번 채우기 
    for x in range(i + w, n):
        for y in range(j - w + h):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 4 

    # 5번 채우기 
    for x in range(i + h + 1, n):
        for y in range(n - 1, j - w + h, -1):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 5
        
def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

# 지역별 인구수 계산, 최대 - 최소
def calc():
    total = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        for j in range(n):
            total[numbers[i][j]] += board[i][j]
    
    # 직사각형 내부 1번 처리 
    total[1] += total[0]
    total.pop(0) # min 계산하기위해 제거

    return (max(total) - min(total))

# 1. 가로, 세로 설정 
for w in range(1, 2 * n):
    for h in range(1, 2 * n):
        # 2. 시작 좌표 설정 (맨 위)
        for i in range(n):
            for j in range(n):
                # 3. 범위 확인 (상, 좌, 하, 우)
                if in_range(i, j) and in_range(i + w, j - w) and \
                in_range(i + w + h, j - w + h) and in_range(i + h, j + h):
                    numbers = [[0 for _ in range(n)] for _ in range(n)]
                    # 4. 경계 표시 
                    draw()
                    # 5. 구역별 인구수 계산, 갱신
                    ans = min(ans, calc())

print(ans)