import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(matrix, x, y, value):
    matrix[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] == value:
                dfs(matrix, nx, ny, value)


N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]  # people(R,G,B)
grid2 = [[0] * N for _ in range(N)]  # people(R=G, B)

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R' or grid[i][j] == 'G':
            grid2[i][j] = 1
        else:
            grid2[i][j] = 2

rgb_count = 0
b_count = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            dfs(grid, i, j, grid[i][j])
            rgb_count += 1

        if grid2[i][j] != 0:
            dfs(grid2, i, j, grid2[i][j])
            b_count += 1

print(rgb_count, b_count)
