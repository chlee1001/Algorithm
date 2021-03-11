import heapq
import sys

input = sys.stdin.readline

n = int(input())
input_list = []

for _ in range(n):
    input_list.append(int(input()))

new_list = []

for num in input_list:
    if num == 0:
        if not new_list:
            print(0)
        else:
            print(-heapq.heappop(new_list))
    else:
        heapq.heappush(new_list, -num)
