import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
# matrix 배열
matrix = [list(map(int, input().rstrip())) for _ in range(N)]

# 이동할 네 방향 정의 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))  # 시작점 (0,0)
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 탐색 공간 내에서만
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아닌경우
                if matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    matrix[nx][ny] = matrix[x][y] + 1
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return matrix[N - 1][M - 1]


print(bfs(0, 0))
