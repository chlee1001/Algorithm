import sys
from collections import deque

N, K = map(int, input().split())
people_deque = deque([i for i in range(1, N + 1)])

print("<", end="")
while people_deque:
    for _ in range(K - 1):
        people_deque.append(people_deque[0])
        people_deque.popleft()
    print(people_deque.popleft(), end="")
    if people_deque:
        print(',', end=" ")
print(">", end="")
