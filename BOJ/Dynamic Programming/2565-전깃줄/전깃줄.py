import sys

input = sys.stdin.readline

line = int(input())
lines_list = [list(map(int, input().split())) for _ in range(line)]

lines_list.sort(key=lambda x: x[0])

dp = [1] * line

for i in range(line):
    for j in range(i):
        if lines_list[i][1] > lines_list[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(line - max(dp))
