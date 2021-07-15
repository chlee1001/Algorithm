import sys

input = sys.stdin.readline

input_string = list(input().rstrip())

values = {'H': 1, 'C': 12, 'O': 16}
stack = []
tmp = 0
for x in input_string:
    if x == '(':
        stack.append(x)
    elif x == ')':
        tmp = 0
        while stack[-1] != '(':
            num = stack.pop()
            tmp += num
        stack.pop()
        stack.append(tmp)
    elif x.isdigit():
        tmp = stack.pop()
        stack.append(tmp * int(x))
    else:
        stack.append(values[x])

print(sum(stack))
