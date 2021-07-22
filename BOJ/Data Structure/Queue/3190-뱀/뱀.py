import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [[0] * (N) for _ in range(N)]  # NxN 보드 생성

K = int(input())  # 사과 개수
for _ in range(K):  # 사과 위치 지정 0:없음, 1:있음
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2

# 우, 하, 좌, 상 // 시계방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

L = int(input())  # 방향 전환 횟수
times = deque()
directions = deque()
for _ in range(L):
    time, dire = input().rstrip().split()
    times.append(int(time))
    directions.append(dire)

nx, ny = 0, 0  # 초기위치
visited = deque([[ny, nx]])

count = 0
direction = 0

while True:
    count += 1
    # 칸 이동
    nx += dx[direction]
    ny += dy[direction]
    if 0 <= nx < N and 0 <= ny < N and board[ny][nx] != 1:  # 보드 체크
        # 사과가 있으면 그냥 추가, 없으면 꼬리 제거하고 추가
        if board[ny][nx] == 0:  # 사과가 없으면
            temp_y, temp_x = visited.popleft()
            board[temp_y][temp_x] = 0  # 꼬리 줄어듬
        board[ny][nx] = 1
        visited.append([ny, nx])

    else:
        print(count)
        exit(0)

    if count in times:
        dire = directions.popleft()
        if dire == 'D':
            direction += 1
            if direction > 3:
                direction = 0
        else:
            direction -= 1
            if direction < 0:
                direction = 3
