n, m, q = map(int, input().split())
board = [[2]*(n+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(n)]+[[2]*(n+2)]
# board = [list(map(int, input().split())) for _ in range(n)]
units = {}
init_k = [0] * (m + 1) # 초기 체력 저장
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

for m in range(1, m + 1):
    units[m] = list(map(int, input().split()))
    init_k[m] = units[m][4]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# start 번호의 기사를 dr 방향으로 밀자
def push_unit(start, dr):
    q = []
    pset = set() # 밀리는 기사 번호 저장
    damage = [0] * (m + 1) # 데미지 누적

    q.append(start) # bfs 준비
    pset.add(start) # 밀리는 기사에 저장

    while q:
        cur = q.pop(0) # 한 명 꺼냄
        ci, cj, h, w, k = units[cur]

        # 명령 받은 방향으로 이동
        # 갈 수 있으면 큐에 삽입 (벽 아닐 경우)
        ni, nj = ci + dxs[dr], cj + dys[dr]
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                # if in_range(i, j):
                    if board[i][j] == 2: # 벽이면 무시
                        return
                    if board[i][j] == 1: # 함정인 경우 데미지 누적
                        damage[cur] += 1

        # 겹치는 경우 큐에 추가 (밀릴 수 있는 경우)
        for idx in units:
            if idx in pset: continue # 이미 대상으로 체크 되어 있어 패스

            ti, tj, th, tw, tk = units[idx] # 현재 노드와 연결된 노드 확인
            # 겹치는 경우
            if ni <= ti + th - 1 and ni + h - 1 >= ti and tj <= nj + w - 1 and nj <= tj + tw - 1:
                q.append(idx)
                pset.add(idx)

    # 명령 받은 기사는 데미지 입지 않음
    damage[start] = 0

    # 데미지 처리
    for idx in pset: # 밀리는 녀석이면
        si, sj, h, w, k = units[idx]

        if k <= damage[idx]: # 체력 보다 더 큰 데미지를 입음
            units.pop(idx)

        else:
            ni, nj = si + dxs[dr], sj + dys[dr] # 이동 시킨 위치 저장
            units[idx] = [ni, nj, h, w, k - damage[idx]]

# main
for _ in range(q):
    idx, dr = map(int, input().split())
    if idx in units: # 명령을 했는데 아직 기사가 살아있다면
        push_unit(idx, dr) # 기사 밀기

ans = 0
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)