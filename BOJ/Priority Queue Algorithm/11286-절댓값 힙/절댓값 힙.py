import sys
import heapq

input = sys.stdin.readline

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))

new_list = []
for nums in num_list:
    if nums == 0:
        if not new_list:
            print(0)
        else:
            print(heapq.heappop(new_list)[1])
    else:
        heapq.heappush(new_list, (abs(nums), nums))
