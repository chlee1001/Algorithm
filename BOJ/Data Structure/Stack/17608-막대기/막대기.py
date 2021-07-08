import sys

input = sys.stdin.readline

N = int(input())

stack = [int(input()) for _ in range(N)]

max_height = 0
cnt = 0
while stack:
    temp = stack.pop()
    if temp > max_height:
        max_height = temp
        cnt += 1

print(cnt)
