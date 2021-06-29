import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and passed[board[nx][ny]] == 0:
            passed[board[nx][ny]] = 1
            dfs(nx, ny, count + 1)
            passed[board[nx][ny]] = 0


R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]
passed = [0] * 26

ans = 1
passed[board[0][0]] = 1
dfs(0, 0, ans)

print(ans)

"""
3 4
ABBC
ECED
FGDH
"""
