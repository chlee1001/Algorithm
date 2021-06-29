import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def DFS(graph, start, visited):
    # 현재 위치 방문처리
    visited[start] = True
    print(start, end=' ')
    for i in range(1, N + 1):
        if not visited[i] and graph[start][i] == 1:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    queue = deque([start])
    # 현재 위치 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True


DFS(graph, V, visited)
visited = [False] * (N + 1)
print()
BFS(graph, V, visited)
