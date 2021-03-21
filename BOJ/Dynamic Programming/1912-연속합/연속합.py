import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [num_list[0]]

for i in range(N - 1):
    dp.append(max(dp[i] + num_list[i + 1], num_list[i + 1]))

print(max(dp))
