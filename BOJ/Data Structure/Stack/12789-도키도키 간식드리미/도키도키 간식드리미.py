import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

init_line = deque(map(int, input().split()))
wait_line = deque()

pos = 1
while init_line:
    if init_line and init_line[0] == pos:
        init_line.popleft()
        pos += 1
    else:
        wait_line.append(init_line.popleft())

    while wait_line and wait_line[-1] == pos:
        wait_line.pop()
        pos += 1

if wait_line:
    print('Sad')
else:
    print("Nice")
