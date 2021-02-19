import sys
import heapq

input = sys.stdin.readline

n = int(input())
card_list = []
for _ in range(n):
    heapq.heappush(card_list, int(input()))

result = 0

while len(card_list) > 1:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    heapq.heappush(card_list, a + b)
    result += (a + b)

print(result)
