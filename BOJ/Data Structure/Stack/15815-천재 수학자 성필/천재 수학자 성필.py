import sys

input = sys.stdin.readline

input_string = input().rstrip()

stack = []

for x in input_string:
    if x.isdigit():
        stack.append(int(x))
    else:
        num2, num1 = stack.pop(), stack.pop()
        if x == '+':
            stack.append(num1 + num2)
        elif x == '-':
            stack.append(num1 - num2)
        elif x == '/':
            stack.append(num1 // num2) # 정수형임으로 //
        elif x == '*':
            stack.append(num1 * num2)

print(stack[0])
