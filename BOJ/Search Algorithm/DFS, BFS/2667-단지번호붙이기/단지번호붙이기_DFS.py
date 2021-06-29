import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, house):
    ground[x][y] = 0  # 해당 지점은 확인

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if ground[nx][ny] == 1:
                house = dfs(nx, ny, house + 1)
    return house


N = int(input())
ground = [list(map(int, input().rstrip())) for _ in range(N)]
houses = []  # 각 단지내 집의 수

for i in range(N):
    for j in range(N):
        if ground[i][j] == 1:
            houses.append(dfs(i, j, 1))

print(len(houses))
for house in sorted(houses):
    print(house)
