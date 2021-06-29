import sys
from collections import deque

input = sys.stdin.readline


def BFS(graph, start):
    queue = deque([start])

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        position = queue.popleft()
        if position == K:
            return graph[position]
        for nx in (position - 1, position + 1, position * 2):
            if 0 <= nx <= MAX and not graph[nx]:
                graph[nx] = graph[position] + 1
                queue.append(nx)


MAX = 10 ** 5
N, K = map(int, input().split())
lines = [0] * (MAX + 1)

print(BFS(lines, N))
