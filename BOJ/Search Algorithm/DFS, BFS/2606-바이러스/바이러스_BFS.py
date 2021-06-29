import sys
from collections import deque

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


def bfs(network, start):
    queue = [start]
    while queue:
        for i in network[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


visited = []
bfs(networks, 1)
print(len(visited) - 1)
