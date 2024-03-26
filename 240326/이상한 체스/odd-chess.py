# 0: 빈 칸, 1 ~ 5 : 자신의 말, 6: 상대의 말
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

horse = {
    # 말 번호: [[[첫번재_dx], [첫번째_dy]], [[두번째_dx], [두번째_dy]]]
    1: [
        [[-1], [0]], [[0], [1]], [[1], [0]], [[0], [-1]]
    ], 
    2: [
        # % 연산 필요 
        [[0, 0], [-1, 1]],
        [[-1, 1], [0, 0]]
    ],
    3: [
        [[-1, 0], [0, 1]],
        [[0, 1], [1, 0]],
        [[0, 1], [-1, 0]], 
        [[0, -1], [-1, 0]]
    ],
    4: [
        [[0, -1, 0], [-1, 0, 1]],
        [[-1, 0, 1], [0, 1, 0]],
        [[0, 1, 0], [-1, 0, 1]],
        [[-1, 0, 1], [0, -1, 0]]
    ],
    5: [
        # % 연산 필요
        [[0, 0, 1, -1], [-1, 1, 0, 0]]
    ]
}

my = [
    (i, j, board[i][j])
    for i in range(n)
    for j in range(m)
    if 1 <= board[i][j] <= 5
]
length = len(my)

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    return True

# 남은 칸 걔산
def calc(board):
    cnt = sum(
        1
        for i in range(n)
        for j in range(m)
        if not board[i][j]
    )
    return cnt

def simulation(choose):
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[i][j]

    # 1. my를 돌며 choose로 선택된 방향으로 이동 (확장)
    for i in range(length):
        d = choose[i]
        x, y, h = my[i]

        if h == 2:
            d %= 2
        elif h == 5:
            d = 0

        move = horse[h][d]
        for dxs, dys in zip(move[0], move[1]):
            # 확장 
            meet_six = False
            for a in range(1, n + 1):
                for b in range(1, m + 1):
                    nx, ny = x + (a * dxs), y + (b * dys)
                    if in_range(nx, ny):
                        if temp[nx][ny] == 6 or meet_six:
                            meet_six = True
                        else: 
                            temp[nx][ny] = '*'

    # 2. 남은 칸 계산 
    return calc(temp)


# main 
# 움직일 말 마다 방향을 모두 정함 - 백트래킹
ans = float('inf')
choose = []
def choice(num):
    global ans
    if num == len(my):
        ans = min(ans, simulation(choose))
        return 

    # 선택 
    for i in range(4):
        choose.append(i)
        choice(num + 1)
        choose.pop()
    

choice(0)
print(ans)