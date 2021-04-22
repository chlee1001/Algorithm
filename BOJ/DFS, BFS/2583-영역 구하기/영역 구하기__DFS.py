import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 방향정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, count):
    ground[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if ground[nx][ny] == 0:
                count = dfs(nx, ny, count + 1)
    return count


M, N, K = map(int, input().split())
ground = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            ground[i][j] = 1

count = []
for i in range(M):
    for j in range(N):
        if ground[i][j] == 0:
            count.append(dfs(i, j, 1))

print(len(count))
for x in sorted(count):
    print(x, end=" ")
