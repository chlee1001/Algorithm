import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while tomatoes:
        x, y = tomatoes.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and boxes[nx][ny] == 0:
                boxes[nx][ny] = boxes[x][y] + 1
                tomatoes.append((nx, ny))


tomatoes = deque()
for i in range(M):
    for j in range(N):
        if boxes[i][j] == 1:
            tomatoes.append((i, j))

bfs()

alreadyTrue = False
count = 0
for row in boxes:
    for tomato in row:
        if tomato == 0:
            alreadyTrue = True
        count = max(count, tomato)

if alreadyTrue:
    print(-1)
elif count == -1:
    print(0)
else:
    print(count - 1)
