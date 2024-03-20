n = int(input())
friends = [
    list(map(int, input().split()))
    for _ in range(n * n)
]

board = [[0] * n for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
# like_friend_list: 인덱스 번호로 접근할 수 있도록
like_friend_list = friends[:]
like_friend_list.sort()
like_friend_list.insert(0, [])

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    return True

# 빈 부분 돌며 좋아하는 친구 수 계산 
def like(f, like_friend):
    me = f[0]
    friend = f[1:]
    for x in range(n):
        for y in range(n):
            # 빈 칸이면 친구 숫자 세기 
            cnt = 0 # 친구 수 저장
            if not board[x][y]:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny):
                        if board[nx][ny] in friend:
                            cnt += 1 
            like_friend[x][y] = cnt
                
def loc(like_friend):
    global board
    loc_list = []
    # 1. 격자 내 4방향 중 좋아하는 친구가 가장 많은 칸
    maximum = max(
        like_friend[i][j]
        for i in range(n)
        for j in range(n)
    )

    for i in range(n):
        for j in range(n):
            if like_friend[i][j] == maximum and not board[i][j]:
                loc_list.append((i, j))

    if len(loc_list) == 1:
        x, y = loc_list[0]
        if not board[x][y]:
            return loc_list[0]

    # 2. 여러개면 4방향 중 빈칸 가장 많은 곳 
    empty = []
    for x, y in loc_list:
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and board[nx][ny] == 0:
                cnt += 1
        empty.append(cnt)
    
    empty_max = max(empty)
    empty_list = [] # 빈 칸 최대 개수 입력 
    for idx, e in enumerate(empty):
        if e == empty_max:
            empty_list.append(loc_list[idx])
    if len(empty_list) == 1:
        x, y = empty_list[0]
        if not board[x][y]:
            return empty_list[0]

    # 3. 행 작은 거, 열 작은거 정렬 
    empty_list.sort(key = lambda x : (x[0], x[1]))
    for e in empty_list:
        if board[e[0]][e[1]] == 0:
            return e

    return -1, -1 

def insert(f):
    like_friend = [[0] * n for _ in range(n)] # 좋아하는 친구 수 계산

    # 1. 빈 부분 돌며 좋아하는 친구 수 계산 
    like(f, like_friend)

    # 2. 들어갈 곳 판단 (조건 4가지 고려), 들어가기
    x, y = loc(like_friend)
    board[x][y] = f[0]

def calc():
    score = [0, 1, 10, 100, 1000]
    total = 0
    for x in range(n):
        for y in range(n):
            cnt = 0 # 인접 친구 개수 
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    if board[nx][ny] in like_friend_list[board[x][y]][1:]:
                        cnt += 1

            if cnt > 0:
                total += (10 ** (cnt - 1)) 
    return total

# main 
ans = 0
for f in friends:
    insert(f)

ans = calc()
print(ans)