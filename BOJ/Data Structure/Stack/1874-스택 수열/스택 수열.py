import sys

input = sys.stdin.readline

N = int(input())

stack = []
count = 0
result = []
flag = 1
for i in range(N):
    temp = int(input())

    while count < temp:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == temp:
        stack.pop()
        result.append('-')
    else:
        flag = 0
        print('NO')
        break

if flag:
    print('\n'.join(result))
