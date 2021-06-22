import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

snail = [[0 for _ in range(N)] for _ in range(N)]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하, 우, 상, 좌

cur_num = N ** 2
cur_x, cur_y = 0, 0
direction = 0
while cur_num > 0:
    snail[cur_y][cur_x] = cur_num
    ny, nx = move[direction]
    dx = cur_x + nx
    dy = cur_y + ny
    if 0 > dx or dx >= N or 0 > dy or dy >= N or snail[dy][dx] != 0:  # 갈 수 없는 곳만 (방문했던 곳X, 벽X)
        direction = (direction + 1) % 4

    ny, nx = move[direction]
    cur_x += nx
    cur_y += ny
    cur_num -= 1

temp_x, temp_y = 0, 0
for i in range(N):
    for j in range(N):
        if snail[i][j] == M:
            temp_x = j
            temp_y = i
        print(snail[i][j], end=" ")
    print()
print(temp_y + 1, temp_x + 1)
