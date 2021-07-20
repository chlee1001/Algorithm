import sys
from collections import deque

input = sys.stdin.readline

s_time, j_time, customer_count = map(int, input().split())  # 상민 포장시간, 지수 포장시간, 손님수
sangmin = deque()  # 상민 포장시작 시간 리스트
jisu = deque()  # 지수 포장시작 시간 시간 리스트
s_end, j_end = 0, 0  # 상민, 지수 포장 끝난 시간

for _ in range(customer_count):
    start_time, color, present_count = input().rstrip().split()  # 주문시각, 색깔, 개수
    start_time = int(start_time)

    if color == 'B':  # 상민

        # 상민 포장 주문시각이 포장끝난 시각보다 먼저일 경우
        # 주문시각(포장시작시각)을 포장끝난 시점으로 변경해준다.
        start_time = max(start_time, s_end)

        for i in range(int(present_count)):  # 주문 개수만큼 반복
            sangmin.append([start_time, 'B'])  # 상민 포장시작 시간 리스트에 저장
            start_time += s_time  # 기존 포장시작시간에 포장에 걸리는 시간 더하기
            s_end = start_time  # 포장끝난 시간은 포장시작시간+포장에 걸리는 시간

    elif color == 'R':  # 지수
        start_time = max(start_time, j_end)

        for i in range(int(present_count)):
            jisu.append([start_time, 'R'])
            start_time += j_time
            j_end = start_time

total_list = sangmin + jisu
total_list = sorted(total_list, key=lambda x: [x[0], x[1]])

s_present, j_present = [], []  # 상민, 지수가 포장한 선물리스트

for idx, present in enumerate(total_list):
    if present[1] == 'B':
        s_present.append(idx + 1)
    else:
        j_present.append(idx + 1)

print(len(s_present))
print(*s_present)
print(len(j_present))
print(*j_present)
