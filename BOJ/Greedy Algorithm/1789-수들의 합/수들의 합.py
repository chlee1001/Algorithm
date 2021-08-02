import sys

input = sys.stdin.readline

S = int(input())

N, i = 0, 1
while True:
    N += i
    if N >= S:
        break
    i += 1

print(i - 1)
