import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
cards_list = list(map(int, input().split()))

result = list(combinations(cards_list, 3))

max_sum = 0
for cards in result:
    temp_sum = sum(cards)
    if m >= temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)
