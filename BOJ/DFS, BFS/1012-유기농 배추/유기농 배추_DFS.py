import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    ground[x][y] = 0 # 해당 지점은 확인

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        else:
            if ground[nx][ny] == 1:
                dfs(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
