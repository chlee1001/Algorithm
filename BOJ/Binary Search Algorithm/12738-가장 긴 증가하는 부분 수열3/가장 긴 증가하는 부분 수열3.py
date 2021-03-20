import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [0]

for i in range(N):
    start = 0
    end = len(dp) - 1

    while start <= end:
        mid = (start + end) // 2
        if num_list[i] > dp[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if start >= len(dp):
        dp.append(num_list[i])
    else:
        dp[start] = num_list[i]

print(len(dp) - 1)
