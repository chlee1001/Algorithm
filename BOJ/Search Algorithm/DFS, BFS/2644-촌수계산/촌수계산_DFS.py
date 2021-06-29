import sys

input = sys.stdin.readline

N = int(input())
comp1, comp2 = map(int, input().split())
M = int(input())
family = {}
for i in range(N):
    family[i + 1] = set()
for i in range(M):
    x, y = map(int, input().split())
    family[x].add(y)
    family[y].add(x)


def dfs(graph, target, count):
    visited[target] = count
    for i in graph[target]:
        if not visited[i]:
            dfs(graph, i, count + 1)


visited = [False] * (N + 1)
dfs(family, comp2, 1)
if not visited[comp1]:
    print(-1)
else:
    print(visited[comp1] - 1)
