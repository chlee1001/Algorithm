import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global count
    queue = set()
    queue.add((0, 0, board[0][0]))

    while queue:
        x, y, ans = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in ans:
                queue.add((nx, ny, ans + board[nx][ny]))
                count = max(count, len(ans) + 1)


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
count = 1
bfs()
print(count)

"""
3 4
ABBC
ECED
FGDH
"""
