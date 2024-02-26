n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def happy_row(num):
    cnt = 1
    ret = 1
    for j in range(n - 1):
        if board[num][j] == board[num][j + 1]:
            cnt += 1
            ret = max(ret, cnt)
        else: 
            cnt = 1

    if ret >= m:
        return 1
    else:
        return 0

def happy_col(num):
    cnt = 1
    ret = 1
    for j in range(n - 1):
        if board[j][num] == board[j + 1][num]:
            cnt += 1
            ret = max(ret, cnt)
        else: 
            cnt = 1
            
    if ret >= m:
        return 1
    else:
        return 0

ans = 0
for i in range(n):
    ans += happy_row(i)
    ans += happy_col(i)

print(ans)