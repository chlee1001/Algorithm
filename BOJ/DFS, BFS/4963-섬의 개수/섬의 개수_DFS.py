import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 방향정의 (상,하,좌,우, 1,5,7,9)
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]


def dfs(x, y):
    ground[x][y] = -1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and ground[nx][ny] == 1:
            dfs(nx, ny)


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    ground = [list(map(int, input().split())) for _ in range(H)]

    count = 0
    for i in range(H):
        for j in range(W):
            if ground[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
