n = int(input())
nums = list(map(int, input().split()))

cnt = 0
minimum = float('inf')

def choose(num):   
    global cnt, minimum
    if num >= n:
        if num == n:
            minimum = min(cnt, minimum)
        return 
    
    for i in range(1, nums[num - 1] + 1):
        cnt += 1
        choose(num + i)
        cnt -= 1

choose(1)
print(-1) if minimum == float('inf') else print(minimum)