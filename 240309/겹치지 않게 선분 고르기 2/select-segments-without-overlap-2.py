n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

# dp[i]: x1 기준으로 정렬되어 있다는 가정 하에 
# i 번째 선분을 끝으로 
# 겹치지 ㅇ낳게 선택할 수 있는 최대 선분의 수 
dp = [0] * n

# 시작점 기준으로 오름차순 정렬 
lines.sort()

for i in range(n):
    dp[i] = 1 # 현재 선분이 시작 선분인 경우에 dp 값은 1

    # i 번째 선택 전 바로 직전에 선택한 선분 j
    # i, j가 겹치지 않고 선택할 수 있는 선분의 최대 개수 계산 
    for j in range(i):
        x1_i, _ = lines[i]
        _, x2_j = lines[j]

        # 이미 정렬되어 있기에 x2[j] < x1[i] 이면 겹치지 않음 
        if x2_j < x1_i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))