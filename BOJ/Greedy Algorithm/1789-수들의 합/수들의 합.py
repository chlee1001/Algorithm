import sys

input = sys.stdin.readline

S = int(input())

N, i = 0, 1
while True:
    N += i
    if N > S:
        print(i - 1)
        break
    elif N == S:
        print(i)
        break
    i += 1
