n = int(input())
MOD = 1000000007
dp = [0] * 1001

dp[0] = 1
dp[1] = 2
dp[2] = 7


# dp[i] = dp[i - 1] * 2 + dp[i - 2] * 3 +
#         (dp[i - 3] + dp[i - 4] + dp[i - 5] + ... dp[0]) * 2
# (A + B) mod C = ((A mod C) + (B mod C)) mod C
for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2]) % MOD
    for j in range(i - 3, -1, -1):
        dp[i] = (dp[i] + 2 * dp[j]) % MOD

print(dp[n])