import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
K = int(input())

card_list = []
for _ in range(N):
    card_list.append(input().rstrip())

result = []
for x in permutations(card_list, K):
    result.append(''.join(x))

result = list(set(result))
print(len(result))
