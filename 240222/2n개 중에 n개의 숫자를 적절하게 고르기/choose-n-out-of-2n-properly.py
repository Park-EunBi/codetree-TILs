n = int(input())
nums = list(map(int, input().split()))

ans = float('inf')

def calc():
    cal = 0
    for num in nums:
        if num not in choice:
            cal += num 
    
    return abs(sum(choice) - cal) 


choice = []
def choose(idx, num):
    global ans
    if num == n:
        ans = min(ans, calc())
        return 

    for i in range(idx, 2* n):
        choice.append(nums[i])       
        choose(i + 1, num + 1)
        choice.pop()


choose(0, 0)
print(ans)