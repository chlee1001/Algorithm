import sys

input = sys.stdin.readline

N, M = map(int, input().split())
result = []


def dfs(idx, depth):
    if depth == M:
        print(*result)
        return
    for i in range(idx, N):
        result.append(i + 1)
        dfs(i, depth + 1)
        result.pop()


dfs(0, 0)
