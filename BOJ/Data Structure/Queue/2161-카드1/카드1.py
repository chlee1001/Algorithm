import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

card_deque = deque([i for i in range(1, N + 1)])
removed_card = []

while len(card_deque) > 0:
    removed_card.append(card_deque.popleft())
    card_deque.rotate(-1)

print(*removed_card)
