# 1: 폭탄, 0: 땅
n = int(input())
board= [list(map(int, input().split())) for _ in range(n)]

bomb = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j]
]

explosion = [
    [(-1, 0), (-2, 0), (1, 0), (2, 0)],
    [(1, 0), (-1, 0), (0, 1), (0, -1)],
    [(-1, -1), (1, 1), (-1, 1), (1, -1)]
]

visited = [[0 for _ in range(n)] for _ in range(n)]

choice = []
maximum = -1

def attack():
    
    for k in range(len(bomb)):
        x, y = bomb[k]
        choosen_bomb = explosion[choice[k]]
        for choosen in choosen_bomb:
            dx, dy = choosen[0], choosen[1]
            nx, ny = x + dx, y + dy
            visited[x][y] = 1
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            visited[nx][ny] = 1

    cnt = 0 
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt += 1

    return cnt

def choose(num):
    global maximum
    if num == len(bomb):
        # 초기화 
        for i in range(n):
            for j in range(n):
                visited[i][j] = 0

        maximum = max(maximum, attack())

        return 

    # 선택 
    for i in range(0, 3):
        choice.append(i)
        choose(num + 1)
        choice.pop()

choose(0)
print(maximum)