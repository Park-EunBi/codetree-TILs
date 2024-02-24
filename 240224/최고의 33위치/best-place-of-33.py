# 1: 동전, 0: 빈칸 

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 격자 내 동전의 수 계산
def calc(x, y):
    total = 0
    for a in range(x, x + 3):
        for b in range(y, y + 3):
            if board[a][b]:
                total += 1
    return total

# 격자의 시작점 완전탐색
for i in range(n-2):
    for j in range(n-2):
        ans = max(ans, calc(i, j))

print(ans)