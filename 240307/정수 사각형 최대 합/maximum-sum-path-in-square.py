n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

# 1. 초깃값 
dp[0][0] = board[0][0]
# 0 열 
for j in range(1, n):
    dp[0][j] = board[0][j] + dp[0][j - 1]
# 0 행 
for i in range(1, n):
    dp[i][0] = board[i][0] + dp[i - 1][0]

# 2. 점화식 
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(board[i][j] + dp[i-1][j], board[i][j] + dp[i][j-1])

print(dp[n-1][n-1])