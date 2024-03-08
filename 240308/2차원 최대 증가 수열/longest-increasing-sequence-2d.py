n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 모두 1로 초기화 한다면 맨 위에서 이동 불가해도 아래에서 이동 가능하면 이동 가능으로 계산
dp = [[-float('inf')] * m for _ in range(n)] 
dp[0][0] = 1 
ans = -1

# 도착지 설정
for i in range(1, n):
    for j in range(1, m): 
        # dp 갱신 
        # 출발지 설정
        for x in range(0, i):
            for y in range(0, j):               
                if board[i][j] > board[x][y]:
                    dp[i][j] = max(dp[i][j], dp[x][y] + 1)

for d in dp:
    ans = max(ans, max(d))

print(ans)

'''
4 4
9 1 1 1
1 2 1 1
1 1 3 1
1 1 1 4

1
'''

'''
5 6
26 14 3 7 13 30
7 1 6 3 30 9
28 13 6 27 18 4
24 3 1 7 1 24
20 26 29 9 3 8

2
'''