import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = []
    flag = 1

    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] == '[':
                flag = 0
                break
            elif stack[-1] == '(':
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] == '(':
                flag = 0
                break
            elif stack[-1] == '[':
                stack.pop()

    if flag == 1 and not stack:
        print('yes')
    else:
        print('no')
