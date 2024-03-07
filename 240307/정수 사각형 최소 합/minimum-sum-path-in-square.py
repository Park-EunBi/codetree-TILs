n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

# 1. 초기화 
dp[0][n-1] = board[0][n-1]
# 0 행 
for j in range(n-2, -1, -1):
    dp[0][j] = board[0][j] + dp[0][j + 1]
# n-1 열
for i in range(1, n):
    dp[i][n-1] = board[i][n-1] + dp[i - 1][n - 1]

# 2. 점화식 
for i in range(1, n):
    for j in range(n-2, -1, -1):
        # print(i, j)
        dp[i][j] = min(board[i][j] + dp[i-1][j], board[i][j] + dp[i][j + 1])

print(dp[n-1][0])