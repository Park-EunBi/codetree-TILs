n = int(input())
nums = list(map(int, input().split()))

ans = float('inf')

def calc():
    cal_1 = 0
    cal_2 = 0
    
    for i in range(2 * n):
        if i in choice:
            cal_1 += nums[i]
        else:
            cal_2 += nums[i]

    return abs(cal_1 - cal_2)


choice = []
def choose(idx, num):
    global ans
    if num == n:
        ans = min(ans, calc())
        return 

    for i in range(idx, 2* n):
        choice.append(i)       
        choose(i + 1, num + 1)
        choice.pop()


choose(0, 0)
print(ans)