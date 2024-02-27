n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = -float('inf')

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    return True

def is_positive(x, y):
    if board[x][y] > 0: # 0 포함 여부 확인 -> 양수라 0 초과  
        return True
    return False

# 양수 박스인지 확인하고, 크기 반환 
def get_box(x, y, a, b):
    # 박스 내부 확인
    for row in range(x, x + a + 1):
        for col in range(y, y + b + 1):
            # 범위 확인 
            if in_range(row, col):
                # 양수 박스 확인 
                if not is_positive(row, col):
                    return -float('inf')
            else:
                return -float('inf')

    return (a + 1) * (b + 1)


# 1. 시작점 고르기 
for i in range(n):
    for j in range(m):
        # 2. 가로, 세로 길이 정하기 
        for a in range(n):
            for b in range(m):
                # 3. 최댓값 갱신 
                ans = max(ans, get_box(i, j, a, b))

print(-1) if ans == -float('inf') else print(ans)