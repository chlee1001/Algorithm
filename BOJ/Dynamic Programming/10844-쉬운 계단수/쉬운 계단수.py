import sys

input = sys.stdin.readline

dp = [[1 for _ in range(10)]]
for i in range(99):
    dp.append([0 for _ in range(10)])

for i in range(99):
    for j in range(10):
        if 1 <= j < 9:
            dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
        elif j >= 9:
            dp[i + 1][j] = dp[i][j - 1]
        elif j <= 0:
            dp[i + 1][j] = dp[i][j + 1]
# print(dp)
n = int(input())
print((sum(dp[n - 1]) - dp[n - 1][0]) % 1000000000)
