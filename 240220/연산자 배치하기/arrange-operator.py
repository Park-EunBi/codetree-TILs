n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # +, -, * 

ans_min = float('inf')
ans_max = -float('inf')

def calc():
    ans = nums[0]
    for i in range(len(ret)):
        if ret[i] == 0:
            ans += nums[i + 1]
        elif ret[i] == 1:
            ans -= nums[i + 1]
        elif ret[i] == 2:
            ans *= nums[i + 1]
    return ans 

ret = []
# +, -, * 3개의 조합을 만들면 된다 
def choose(num):
    global ans_min, ans_max
    if num == n - 1:
        temp = calc()
        ans_min = min(temp, ans_min)
        ans_max = max(temp, ans_max)
        return  

    for i in range(3): # +, -, *
        if ops[i] <= 0:
            continue
        ops[i] -= 1
        ret.append(i)
        choose(num + 1)
        ret.pop()
        ops[i] += 1

choose(0)
print(ans_min, ans_max)

'''
6
3 3 5 1 3 1 
0 5 0 

-10 -10
'''