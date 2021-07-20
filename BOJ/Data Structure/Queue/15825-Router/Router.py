import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
buffer = deque()
full = 0
while True:
    packet = int(input())

    if packet == -1:
        break
    elif packet == 0:
        buffer.popleft()
        full -= 1
    else:
        if full >= N:
            continue
        else:
            buffer.append(packet)
            full += 1

if buffer:
    print(*buffer)
else:
    print("empty")
