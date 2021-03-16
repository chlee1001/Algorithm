import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [1] * N
inverse_dp = [1] * N

for i in range(N):
    for j in range(i):  # j<i
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if num_list[j] < num_list[i]:
            inverse_dp[i] = max(inverse_dp[i], inverse_dp[j] + 1)

new_dp = [0] * N
for i in range(N):
    new_dp[i] = dp[i] + inverse_dp[i] - 1
print(max(new_dp))
