import sys
from bisect import bisect_left

input = sys.stdin.readline

N, H = map(int, input().split())

down = []
up = []
for i in range(N):
    if i % 2 == 0:  # 짝수: 석순
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()

min_count = N
result = 0

for i in range(1, H + 1):
    down_count = len(down) - bisect_left(down, i - 0.5)
    up_count = len(up) - bisect_left(up, H - i + 0.5)

    if min_count == down_count + up_count:
        result += 1
    elif min_count > down_count + up_count:
        result = 1
        min_count = down_count + up_count

print(min_count, result)
