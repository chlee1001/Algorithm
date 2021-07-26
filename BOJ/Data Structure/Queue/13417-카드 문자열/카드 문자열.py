import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    card_list = deque(input().rstrip().split())
    new_list = deque(card_list.popleft())

    while card_list:
        temp = card_list.popleft()
        if temp > new_list[0]:
            new_list.append(temp)
        else:
            new_list.appendleft(temp)

    print(''.join(new_list))
