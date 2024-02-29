n = int(input())
nums = []
for _ in range(n):
    nums.insert(0, int(input()))

removes = [tuple(map(int, input().split())) for _ in range(2)]

for i in range(2):
    s, e = removes[i]
    for j in range(e - s + 1):
        nums.pop(len(nums) - s)

print(len(nums))
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])