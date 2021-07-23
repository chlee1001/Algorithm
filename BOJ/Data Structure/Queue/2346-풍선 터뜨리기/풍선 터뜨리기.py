import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

balloons = [x for x in range(1, N + 1)]
papers = list(map(int, input().split()))

bomb = deque()
for balloon, paper in zip(balloons, papers):
    bomb.append([balloon, paper])

while bomb:
    balloon, paper = bomb.popleft()
    print(balloon, end=" ")
    if bomb:
        if paper > 0:
            for _ in range(paper - 1):
                bomb.append(bomb.popleft())
        else:
            for _ in range(-paper):
                bomb.appendleft(bomb.pop())
