n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * m for _ in range(n)]

# 도착지 설정
for i in range(1, n):
    for j in range(1, m): 
        # dp 갱신 
        # 출발지 설정
        for x in range(0, i):
            for y in range(0, j):
                if board[i][j] > board[x][y]:
                    dp[i][j] = max(dp[i][j], dp[x][y] + 1)

ans = -1
for d in dp:
    ans = max(ans, max(d))

print(ans)