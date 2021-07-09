import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = list(input().rstrip())
    left, right = [], []

    for x in stack:
        if x == '<':
            if left:
                right.append(left.pop())
        elif x == '>':
            if right:
                left.append(right.pop())
        elif x == '-':
            if left:
                left.pop()
        else:
            left.append(x)

    if right:
        left.extend(reversed(right))

    print(''.join(left))
