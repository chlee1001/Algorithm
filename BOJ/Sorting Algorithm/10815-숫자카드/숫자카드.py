import sys

input = sys.stdin.readline


def binary_search(own_cards, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == own_cards[mid]:
        return 1
    elif target > own_cards[mid]:
        return binary_search(own_cards, target, mid + 1, end)
    else:
        return binary_search(own_cards, target, start, mid - 1)


n = int(input())
own_cards = list(map(int, input().split()))

m = int(input())
check_cards = list(map(int, input().split()))

own_cards.sort()
for i in range(m):
    if binary_search(own_cards, check_cards[i], 0, n - 1) == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")
