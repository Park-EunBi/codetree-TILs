n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
ans = -float('inf')

def calc():
    temp = 0
    for c in choice:
        temp ^= c
    return temp


choice = []
def choose(idx, num): # 사용한 nums의 인자의 자릿수, 현재 자릿수 
    global ans
    if num == m:
        ans = max(ans, calc())
        return 

    for i in range(idx, n):
        choice.append(nums[i])
        choose(i + 1, num + 1)
        choice.pop()

choose(0, 0)
print(ans)