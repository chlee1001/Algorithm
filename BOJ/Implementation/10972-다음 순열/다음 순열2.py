import sys

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if num_list[i] > num_list[i - 1]:  # 뒷 값이 앞에 값보다 크면
        for j in range(N - 1, 0, -1):
            if num_list[j] > num_list[i - 1]:
                num_list[j], num_list[i - 1] = num_list[i - 1], num_list[j]  # 교체해주고 그 뒷부분은 정렬시킴
                num_list = num_list[:i] + sorted(num_list[i:])
                print(*num_list)
                exit(0)

print(-1)
