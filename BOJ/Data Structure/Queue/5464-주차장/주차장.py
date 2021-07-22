import sys
from collections import deque
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
# N~: 단위 무게당 요금을 나타내는 정수, N: 주차공간 1,2,3....
# M~: 차량들의 무게

fees = [int(input()) for _ in range(N)]  # 요금 리스트
weights = [int(input()) for _ in range(M)]  # 무게 리스트

parking = {}  # 주차 된 차량 정보들
for i in range(M + 1):
    parking[i + 1] = []

waiting = deque()  # 기다리는 차량

parking_idx = [x for x in range(N)]  # 주차공간(번호)
heapq.heapify(parking_idx)

total_fee = 0
for i in range(2 * M):
    if parking_idx and waiting:  # 첫 번째, 주차공간과 기다리는 차량이 있는 경우
        car_num = waiting.popleft()  # 첫 번째로 기다리고 있는 차량 번호
        idx = heapq.heappop(parking_idx)  # 주차공간(번호) 부여
        parking[car_num] = [idx, fees[idx], weights[car_num - 1]]  # 주차정보 기입

    car_num = int(input())  # 차량번호
    if car_num > 0:  # 입차
        if parking_idx:  # 주차공간 있으면
            idx = heapq.heappop(parking_idx)
            parking[car_num] = [idx, fees[idx], weights[car_num - 1]]
        else:
            waiting.append(car_num)

    else:  # 출차
        car_num = abs(car_num)
        idx = parking[car_num][0]
        fee = parking[car_num][1]
        weight = parking[car_num][2]
        total_fee += fee * weight
        heapq.heappush(parking_idx, idx)  # 출차로 인해 주차공간 생김

print(total_fee)
