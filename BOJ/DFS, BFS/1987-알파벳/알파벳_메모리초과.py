import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global count
    count = max(cnt, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in passed:
            passed.append(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            passed.append(board[nx][ny])


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
passed = []
count = 1
dfs(0, 0, count)
print(count)

"""
3 4
ABBC
ECED
FGDH
"""
