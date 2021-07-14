import sys

input = sys.stdin.readline

input_string = list(input().rstrip())

left = []
right = []

for x in input_string:
    if x == '(':
        left.append(x)
    elif x == ')':
        if left:
            left.pop()
        else:
            right.append(x)

print(len(left) + len(right))
