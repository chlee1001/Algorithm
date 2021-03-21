import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
num_list = sorted([int(input()) for _ in range(N)])

# for _ in range(N):
#     num_list.append(int(input()))
#
# num_list.sort()

# 산술평균
print(round(sum(num_list) / N))
# 중앙값
print(num_list[N // 2])

# 최빈값
mode_num = Counter(num_list).most_common()
if len(mode_num) > 1:
    if mode_num[0][1] == mode_num[1][1]:
        print(mode_num[1][0])
    else:
        print(mode_num[0][0])
else:
    print(mode_num[0][0])

# 범위
print(num_list[-1] - num_list[0])
