import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

trees = {}
for i in range(N):
    trees[i + 1] = set()

for i in range(N - 1):
    a, b = map(int, input().split())
    trees[a].add(b)
    trees[b].add(a)

parents = [False] * (N + 1)


def dfs(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(graph, i, visited)


dfs(trees, 1, parents)
for i in range(2, N + 1):
    print(parents[i])
