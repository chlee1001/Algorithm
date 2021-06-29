import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M = map(int, input().split())
graph = {}
for i in range(N + 1):
    graph[i] = set()

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

visited = [False] * (N + 1)
component = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        component += 1

print(component)
