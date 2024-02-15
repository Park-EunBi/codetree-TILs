n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

choice_list = [] # 각 항목의 절반은 아침, 절반은 저녁

# 0~total 수 중 num 개의 수를 뽑아서 ret_list에 저장하라 
ret = []
def choice(num, ret_list, total): 
    if len(ret) == num:
        ret_list.append(list(ret))    
        return 

    for i in range(total):
        if i not in ret:
            ret.append(i)
            choice(num, ret_list, total)
            ret.pop()

choice(n, choice_list, n)

def make_sum(cal_list, day):
    # call list 에 담긴 인덱스
    # 계산할 리스트를 받아서 더할 i, j를 뽑아내서 더함 
    temp_sum = 0
    for c in cal_list:
        i = day[c[0]]
        j = day[c[1]]
        temp_sum += board[i][j]
    return temp_sum

diff = float('inf')

for ch in choice_list:
    idx_list = [] 
    morning = ch[:n//2]
    evening = ch[n//2:]

    # 각 항목당 2개씩 뽑아서 더해주기 
    choice(2, idx_list, n//2)
    diff = min(diff, abs(make_sum(idx_list, morning) - make_sum(idx_list, evening)))

print(diff)