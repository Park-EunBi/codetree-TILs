n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(input().split()) for _ in range(q)] # 사용시 첫인자 int로 변환 필수 

# 열 중 같은 값이 있는지 확인 
def is_same_up(line):
    same = False
    for j in range(m):
        if board[line][j] == board[line - 1][j]:
            same = True
    return same

def is_same_down(line):
    same = False
    for j in range(m):
        if board[line][j] == board[line + 1][j]:
            same = True
    return same

def left_wind(line):
    temp = board[line][-1]
    for i in range(m - 1, 0, -1):
        board[line][i] = board[line][i - 1]
    board[line][0] = temp 

def right_wind(line):
    temp = board[line][0]
    for i in range(m - 1):
        board[line][i] = board[line][i + 1]
    board[line][-1] = temp

# main
for i in range(q):
    line, d = winds[i]
    line = int(line) - 1 # index 처리

    # 1. 기본 바람 
    if d == 'L':
        left_wind(line)
    else:
        right_wind(line)

    # 2. 위로 확산  
    for a in range(line, 0, -1):
        if is_same_up(a): # 위의 행과 동일한 값이 있는지 확인 
            if d == 'L':
                right_wind(a - 1)
                d = 'R'
            else:
                left_wind(a - 1)
                d = 'L'
            
        else:
            break # continue

    # 3. 아래로 확산 
    d = winds[i][1]
    for b in range(line, n - 1):
        if is_same_down(b): 
            if d == 'L':
                right_wind(b + 1)
                d = 'R'
            else:
                left_wind(b + 1)
                d = 'L'
        else:
            break

for b in board:
    print(*b)