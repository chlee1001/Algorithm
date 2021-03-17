import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

max_idx = max(dp)
ans = []

for i in range(N - 1, -1, -1):
    if dp[i] == max_idx:
        ans.append(num_list[i])
        max_idx -= 1

ans.reverse()
print(' '.join(map(str, ans)))
