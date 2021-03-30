import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

index_stack = []
result = [-1 for _ in range(N)]  # 각 인덱스에 오큰수를 찾지 못하면 -1

index_stack.append(0)
i = 1

while index_stack and i < N:  # 스택에 값이 존재하며, i가 N보다 작을 때만
    while index_stack and num_list[index_stack[-1]] < num_list[i]:
        result[index_stack[-1]] = num_list[i]
        index_stack.pop()

    index_stack.append(i)
    i += 1

for num in result:
    print(num, end=" ")
