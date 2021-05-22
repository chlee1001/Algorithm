import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]


def BFS(graph, start):
    queue = deque([start])

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        r, c = queue.popleft()
        if r == target_row and c == target_column:
            return graph[r][c]
        for step in steps:
            # 이동하고자 하는 위치 확인
            next_row = r + step[0]
            next_col = c + step[1]
            # 해당 위치로 이동이 가능하다면 카운트 증가
            if 0 <= next_row < I and 0 <= next_col < I and graph[next_row][next_col] == 0:
                graph[next_row][next_col] = graph[r][c] + 1
                queue.append((next_row, next_col))


for _ in range(T):
    I = int(input())
    chess_board = [[0] * (I + 1) for _ in range(I + 1)]

    row, column = map(int, input().split())
    target_row, target_column = map(int, input().split())
    result = BFS(chess_board, (row, column))
    print(result)
