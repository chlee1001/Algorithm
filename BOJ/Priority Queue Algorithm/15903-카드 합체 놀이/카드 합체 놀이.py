import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

heapq.heapify(card_list)  # card_list를 heap으로 변환

for _ in range(M):
    x, y = heapq.heappop(card_list), heapq.heappop(card_list)
    for _ in range(2):
        heapq.heappush(card_list, x + y)


print(sum(card_list))
