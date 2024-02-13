n, m = map(int, input().split())
# 0: 뱀 있, 1: 뱀 없 
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

def canGo(x, y):
    # 1. 격자 내
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    # 2. 장애물, 방문 여부 확인 
    if board[x][y] == 0:
        return False 
    return True

def dfs(x, y):
    # print("dfs({}, {})".format(x, y))
    # if x == n - 1 and y == m - 1:
    #     return True
    
    board[x][y] = 0 # 방문처리 
    for dxs, dys in zip((0, 1), (1, 0)):
        dx, dy = x + dxs, y + dys
        if canGo(dx, dy):
            dfs(dx, dy)

# print(1) if dfs(0, 0) else print(0)
dfs(0, 0)
print(0) if board[n-1][m-1] else print(1)


'''
2 2
1 1
0 1
'''