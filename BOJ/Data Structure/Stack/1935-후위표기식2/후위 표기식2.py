import sys

input = sys.stdin.readline

N = int(input())
postfix = input().rstrip()
num_list = [int(input()) for _ in range(N)]

stack = []
for element in postfix:
    if 'A' <= element <= 'Z':
        stack.append(num_list[ord(element) - ord('A')])
    else:
        num2, num1 = stack.pop(), stack.pop()

        if element == '+':
            stack.append(num1 + num2)
        elif element == '-':
            stack.append(num1 - num2)
        elif element == '*':
            stack.append(num1 * num2)
        elif element == '/':
            stack.append(num1 / num2)

print('%.2f' % stack[0])
