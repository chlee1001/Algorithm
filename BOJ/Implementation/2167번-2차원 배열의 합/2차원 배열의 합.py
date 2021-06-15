import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = matrix[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])
# for _ in range(K):
#     i, j, x, y = map(int, input().split())
#     arr_sum = 0
#     for a in range(i, x + 1):
#         for b in range(j, y + 1):
#             arr_sum += matrix[a - 1][b - 1]
#     print(arr_sum)
