import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
