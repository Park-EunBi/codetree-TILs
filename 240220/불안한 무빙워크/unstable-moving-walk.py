n, k = tuple(map(int, input().split()))
given_row = list(map(int, input().split()))

u = [(0, False) for _ in range(n)] # 위쪽 무빙워크
d = [(0, False) for _ in range(n)] # 아래쪽 무빙워크

for i, stability in enumerate(given_row[:n]):
    u[i] = (stability, False) # (안정성, 사람 유무)
for i, stability in enumerate(given_row[n:]):
    d[i] = (stability, False) # (안정성, 사람 유무)

trial = 0

def shift():
    # 무빙워크 이동 
    temp = u[n - 1]
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]

    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

def canGo(idx):
    # 밖으로 나가기 가능 
    if idx == n:
        return True
    
    # 안정성, 사람 있는지 확인 
    stability, occupied = u[idx]
    return stability > 0 and not occupied

def move(idx):
    # 현재 위치 사람 없애기 
    curr_stablility, _ = u[idx]
    u[idx] = (curr_stablility, False)

    # 범위 내라면 
    if idx + 1 < n:
        # 안정성 감소, 사람 추가 
        next_stability, _ = u[idx + 1]
        u[idx + 1] = (next_stability - 1, True) 

def move_all():
    # 사람 이동 
    for i in range(n - 1, -1, -1):
        _, occupied = u[i]
        # 사람이 있고, 이동 가능하면 (다음칸이 범위 내, 안정성 > 0, 사람 없으면)
        if occupied and canGo(i + 1):
            move(i)

def add():
    stability, occupied = u[0]
    # 안정성 > 0 이고, 사람이 없다면 
    if stability > 0 and not occupied:
        u[0] = (stability - 1, True)

def simulate():
    # 1. 무빙워크 회전 
    shift()

    # 2. 사람 한 칸 이동
    move_all()

    # 3. 새로운 사람 등록
    add()

    # 4. n 번 칸에 사람 있으면 내리기 
    _, occupied = u[n - 1]
    if occupied:
        move(n - 1)

def done():
    # 안정성 < 0 인 부분이 k 개 이상인지 확인 
    unstable_cnt = 0
    for stability, _ in u:
        if not stability:
            unstable_cnt += 1
    
    for stability, _ in d:
        if not stability:
            unstable_cnt += 1
    return unstable_cnt >= k


while not done():
    simulate()
    trial += 1

print(trial)