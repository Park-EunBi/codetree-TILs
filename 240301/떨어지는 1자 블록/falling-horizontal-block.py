# 0: 빈칸, 1: 블럭 
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
k -= 1

# 블록 하강 범위 내 가장 열 인덱스가 작은 곳 찾기 
idx = n + 1
for j in range(k, k + m):
    for i in range(n):
        if board[i][j] == 1:
            idx = min(idx, i)

# 모두 비어있을 때 
if idx == n + 1:
    idx = 0
    
# 블록 채우기 
for j in range(k, k + m):
    board[idx - 1][j] = 1

for b in board:
    print(*b)