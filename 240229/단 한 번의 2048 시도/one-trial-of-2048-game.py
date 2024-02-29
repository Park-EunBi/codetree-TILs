board = [list(map(int, input().split())) for _ in range(4)]
d = input()
temp = [[0 for _ in range(4)] for _ in range(4)]

def move():
    temp = [[0 for _ in range(4)] for _ in range(4)]
    # L
    if d == 'L':
        for i in range(4):
            idx = 0
            for b in board[i]:
                if b:
                    temp[i][idx] = b
                    idx += 1 

    # R
    elif d == 'R':
        for i in range(4):
            idx = 3
            for j in range(3, -1, -1):
                if board[i][j]:
                    temp[i][idx] = board[i][j]
                    idx -= 1 

    # U
    elif d == 'U':
        for j in range(4):
            idx = 0
            for i in range(4):
                if board[i][j]:
                    temp[idx][j] = board[i][j]
                    idx += 1

    # D
    elif d == 'D':
        for j in range(4):
            idx = 3
            for i in range(3, -1, -1):
                if board[i][j]:
                    temp[idx][j] = board[i][j]
                    idx -= 1
    return temp

def merge():
    # L
    if d == 'L':
        for i in range(4):
            for j in range(3):
                if board[i][j] == board[i][j + 1]:
                    board[i][j] *= 2
                    board[i][j + 1] = 0

    # R
    elif d == 'R':
        for i in range(4):
            idx = 3
            for j in range(3, 0, -1):
                if board[i][j] == board[i][j - 1]:
                    board[i][j] *= 2
                    board[i][j - 1] = 0

    # U
    elif d == 'U':
        for j in range(4):
            idx = 0
            for i in range(3):
                if board[i][j] == board[i + 1][j]:
                    board[i][j] *= 2
                    board[i + 1][j] = 0

    # D
    elif d == 'D':
        for j in range(4):
            idx = 3
            for i in range(3, 0, -1):
                if board[i][j] == board[i - 1][j]:
                    board[i][j] *= 2
                    board[i - 1][j] = 0


# 밀기 
board = move()
# 합치기 
merge()
# 다시 밀기 
board = move()

for b in board:
    print(*b)