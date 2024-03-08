n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

# 1. 초기화 
dp[0][0] = board[0][0]
# 0행 
for j in range(1, n):
    dp[0][j] = max(dp[0][j-1], board[0][j])
# 0열 
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], board[i][0])

# 2. 점화식 
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], board[i][j]), max(dp[i][j - 1], board[i][j]))

print(dp[n-1][n-1])