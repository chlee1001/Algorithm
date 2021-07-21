import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M = int(input())
    left_box = deque(map(int, input().split()))
    right_box = deque(map(int, input().split()))

    car_count = 0
    count = 0
    while left_box:
        temp = left_box.popleft()
        if temp + 1000 in right_box:
            count += 1
        if count == 2:
            count = 0
            car_count += 1

    print(car_count)
