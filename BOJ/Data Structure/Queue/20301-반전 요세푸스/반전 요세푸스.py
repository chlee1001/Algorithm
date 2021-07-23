import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())

people = deque(x for x in range(1, N + 1))

while people:
    for _ in range(M):
        people.rotate(-(K - 1))  # 오른쪽
        if not people:
            break
        print(people.popleft())

    for _ in range(M):
        people.rotate(K)  # 왼쪽
        if not people:
            break
        print(people.popleft())
