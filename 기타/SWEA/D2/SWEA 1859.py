import sys

input = sys.stdin.readline

T = int(input())

# Reverse
for testcase in range(T):
    N = int(input())
    num_list = list(map(int, input().split(' ')))

    current_max = num_list[-1]
    answer = 0
    for i in range(len(num_list) - 1, -1, -1):
        if current_max > num_list[i]:
            answer += current_max - num_list[i]
        else:
            current_max = num_list[i]
    print(f'#{testcase + 1} {answer}')

# Inverse 시간 초과
for testcase in range(T):
    N = int(input())
    num_list = list(map(int, input().split(' ')))
    stack_list = num_list[:]

    current_max = max(stack_list)
    answer = 0
    for i in range(len(num_list)):
        stack_list.pop(0)
        if current_max > num_list[i]:
            answer += current_max - num_list[i]
        else:
            if stack_list:
                current_max = max(stack_list)
    print(f'#{testcase + 1} {answer}')
