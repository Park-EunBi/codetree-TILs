n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

# 연속된 수 0 처리 
def bomb(start, end):
    for i in range(start, end + 1):
        nums[i] = 0

# 중력
def down():
    temp = []
    for n in nums:
        if n:
            temp.append(n)
    return temp

# 종료 
def end(before, after):
    if before == after:
        return True
    return False 

# 연속된 수 확인 
def check():
    start_idx, end_idx = 0, 0
    for i in range(len(nums) - 1):

        if nums[i] == nums[i + 1]:
            end_idx = i + 1
        else:
            
            if end_idx - start_idx + 1 >= m:
                bomb(start_idx, end_idx)
            start_idx, end_idx = i + 1, i + 1

    if start_idx != end_idx:
        bomb(start_idx, end_idx)

before = len(nums)
after = -1

while not end(before, after):
    if m == 1:
        nums = []
        break

    if n < m:
        break

    before = len(nums)
    # 폭탄
    check()
    # 중력
    nums = down()
    after = len(nums)

print(len(nums))
for n in nums:
    print(n)