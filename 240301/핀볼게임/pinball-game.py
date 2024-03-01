# 0: 빈 공간, 1: /, 2: \ 
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = -float('inf')
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상

# /
one_dir = {
    0: 3,
    1: 2,
    2: 1, 
    3: 0
}

# \ 
two_dir = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True 

def move(x, y, d):     
    # /
    if board[x][y] == 1:
        d = one_dir[d]
    # \ 
    elif board[x][y] == 2:
        d = two_dir[d]

    nx, ny = x + dxs[d], y + dys[d]
    return nx, ny, d

def simulation(x, y, d):
    global ans
    time = 1

    while in_range(x, y):
        x, y, d = move(x, y, d)
        time += 1

    return time 


# 시작 지점 설정 1. - 행 (i: 0, n-1)
for j in range(n):
    ans = max(ans, simulation(0, j, 1))
    ans = max(ans, simulation(n-1, j, 3))

# 시작 지점 설정 2. - 열 (j: 0, n-1)
for i in range(n):
    ans = max(ans, simulation(i, 0, 0))
    ans = max(ans, simulation(i, n - 1, 2))

print(ans)

'''
3
0 1 1 
0 0 0 
2 2 1

8
'''