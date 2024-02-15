import sys 
INT_MAX = sys.maxsize

n = int(input())
p = [
    list(map(int, input().split()))
    for _ in range(n)
]
evening = [
    False for _ in range(n)
]
ans = INT_MAX

# 아침과 저녁의 차이를 계산 
def calc():
    moring_sum = sum([
        p[i][j]
        for i in range(n)
        for j in range(n)
        if not evening[i] and not evening[j] # 저녁에 해당하지 않는다면 
    ])

    evening_sum = sum([
        p[i][j]
        for i in range(n)
        for j in range(n)
        if evening[i] and evening[j]
    ])

    return abs(moring_sum - evening_sum)

def find_min(curr_idx, cnt):
    global ans

    if cnt == n//2:
        ans = min(ans, calc())
        return 
    
    if curr_idx == n:
        return 

    # curr_idx 업무를 아침에 하는 경우 
    find_min(curr_idx + 1, cnt)

    # curr_idx 업무를 밤에 하는 경우 
    evening[curr_idx] = True # append 
    find_min(curr_idx + 1, cnt + 1) # 재귀
    evening[curr_idx] = False # pop

find_min(0, 0)

print(ans)