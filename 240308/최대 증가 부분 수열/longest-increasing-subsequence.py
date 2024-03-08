n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(n - 1):
        if nums[i] > nums[j]:
            dp[i] = dp[j] + 1

print(max(dp))