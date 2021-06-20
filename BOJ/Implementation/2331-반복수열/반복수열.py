import sys

input = sys.stdin.readline

A, P = map(int, input().split())

stack = [A]
temp = 0
while 1:
    value = str(stack[-1])
    temp = 0
    for i in range(len(value)):
        temp += int(value[i]) ** P

    if temp in stack:
        value = str(stack[-1])
        temp = 0
        for i in range(len(value)):
            temp += int(value[i]) ** P
        break
    else:
        stack.append(temp)

print(stack.index(temp))
