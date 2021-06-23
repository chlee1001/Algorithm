import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sentence = list(input().rstrip().split(" "))
    for x in sentence:
        print(''.join(reversed(list(x))), end=" ")
    print()
