import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))
dp = [num for num in num_list]

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + num_list[i])

print(max(dp))
