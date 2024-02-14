# # 백준 14501
# import sys 
# input = sys.stdin.readline

# n = int(input())
# work = [tuple(map(int, input().split())) for _ in range(n)]

# times = [
#     (i, i + time - 1) # 시작 날짜, 끝나는 시간 
#     for i, (time, _ ) in enumerate(work, start = 1)
# ]

# money = [m for _, m in work]

# selected_job = []
# max_profit = 0

# # 선택 외주 작업에 대한 수익 반환 
# def get_profit():
#     return sum([ # 모두 더해 반환 
#         money[job_idx] # 해당 작업의 수익을 
#         for job_idx in selected_job # 선택한 외주 작업물에 대해
#     ])

# # 외주 작업 수행 가능 여부 판단 
# def is_available():
#     # 이전 외주의 종료일이 다음주 외주 시작일 보다 늦으면 안된다 
#     for i in range(len(selected_job) - 1):
#         _, end_time = times[selected_job[i]]
#         start_time, _= times[selected_job[i + 1]]
#         if end_time >= start_time:
#             return False 

#     # 외주 기간이 휴가 기간을 넘어서는지 판단 
#     for job_idx in selected_job:
#         _, end_time = times[job_idx]
#         if end_time > n:
#             return False 
#     return True

# def find_max_profit(curr_idx):
#     global max_profit

#     # 모든 외주 작업 탐색
#     # 최대 수익 갱신 
#     if curr_idx == n:
#         if is_available():
#             max_profit = max(max_profit, get_profit())
#         return 

#     # 해당 인덱스 외주 작업 안했을 경우 
#     find_max_profit(curr_idx + 1)

#     # 해당 인덱스 외주 작업 했을 경우 
#     selected_job.append(curr_idx)
#     find_max_profit(curr_idx + 1)
#     selected_job.pop()

# find_max_profit(0)
# print(max_profit)

n = int(input())
times = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [0] * (n + 1)

# top-down

for i in range(n-1, -1, -1):
    # 휴가 넘기는 지 확인 
    if i + times[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # 외주 하는 것과 하지 않는 것 중 큰 것 선택
        dp[i] = max(dp[i+1], times[i][1] + dp[i + times[i][0]])

print(dp[0])