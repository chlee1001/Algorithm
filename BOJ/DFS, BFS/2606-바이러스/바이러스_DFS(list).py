import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


computers, edges = int(input()), int(input())

networks = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)

for i in range(edges):
    a, b = map(int, input().split())
    networks[a].append(b)
    networks[b].append(a)

dfs(networks, 1, visited)
print(visited.count(True) - 1)
