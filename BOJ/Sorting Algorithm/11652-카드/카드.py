import sys

input = sys.stdin.readline

N = int(input())

cards = {}
for _ in range(N):
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

cards = sorted(cards.items(), key=lambda x: (-x[1], x[0]))
print(cards[0][0])
