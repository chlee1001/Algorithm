import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[] for _ in range(N)]

# 역순으로...
for i in range(N - 1, -1, -1):  # N-1부터, -1까지, -1씩
    for j in range(len(matrix[i])):
        if i == (N - 1):
            dp[i].append(matrix[i][j])
        else:
            dp[i].append(matrix[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1]))

print(dp[0][0])
