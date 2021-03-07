import sys

input = sys.stdin.readline

n = int(input())

han_number = 0

for i in range(1, n + 1):
    if i <= 99:  # 1부터 99까지는 모두 한수
        han_number += 1
    else:
        nums = list(map(int, str(i)))  # 숫자를 자리수별로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]:
            han_number += 1

print(han_number)
