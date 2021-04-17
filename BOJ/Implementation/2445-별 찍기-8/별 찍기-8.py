import sys

input = sys.stdin.readline

N = int(input())

for i in reversed(range(1, N)):
    print('*' * (N - i) + ' ' * (2 * i) + '*' * (N - i))

for i in range(N):
    print('*' * (N - i) + ' ' * (2 * i) + '*' * (N - i))
