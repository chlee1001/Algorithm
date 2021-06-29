import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

computers = int(input())
edges = int(input())

networks = {}
for i in range(computers):
    networks[i + 1] = set()

for i in range(edges):
    a, b = map(int, input().split())
    networks[a].add(b)
    networks[b].add(a)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * (computers + 1)
dfs(networks, 1, visited)
print(visited.count(True) - 1)
