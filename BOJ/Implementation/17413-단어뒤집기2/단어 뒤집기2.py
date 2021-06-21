import sys

input = sys.stdin.readline

input_string = list(input().rstrip())

temp_stack = []
result = []
flag = 0

for x in input_string:
    if x == '<':
        flag = 1
        temp_stack.append(x)
    elif x == '>':
        flag = 0
        temp_stack.append(x)
        result += temp_stack
        temp_stack = []
    elif x == ' ':
        temp_stack.append(x)
        result += temp_stack
        temp_stack = []
    else:
        if flag == 0:
            temp_stack.insert(0, x)
        elif flag:
            temp_stack.append(x)

result += temp_stack

for x in result:
    print(x, end='')
