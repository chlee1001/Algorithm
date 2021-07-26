import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
card_list = deque(range(1, N + 1))
commands = list(map(int, input().split()))
init_list = deque()

while commands:
    command = commands.pop()
    temp = card_list.popleft()
    if command == 1:
        init_list.appendleft(temp)
    elif command == 2:
        init_list.insert(1, temp)
    elif command == 3:
        init_list.append(temp)

print(*init_list)
