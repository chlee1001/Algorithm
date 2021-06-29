import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and ground[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, h)


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

result = 0
for k in range(max(max(ground))):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if ground[i][j] > k and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dfs(i, j, k)
    result = max(result, count)
print(result)
