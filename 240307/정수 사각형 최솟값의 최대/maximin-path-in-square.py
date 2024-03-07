n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

# 1. 초기화 
dp[0][0] = board[0][0]
# 0행 
for j in range(1, n):
    dp[0][j] = min(board[0][j], dp[0][j-1])
# 0열
for i in range(1, n):
    dp[i][0] = min(board[i][0], dp[i-1][0])

# 2. 점화식
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], board[i][j]), min(dp[i][j-1], board[i][j]))

print(dp[n-1][n-1])