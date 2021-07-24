import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
compare = list(map(int, input().split()))

# 순방향
first_idx = compare.index(sequence[0])  # 기준점
new_list1 = compare[first_idx:] + compare[:first_idx]

# 역방향
compare = compare[::-1]
first_idx = compare.index(sequence[0])  # 기준점
new_list2 = compare[first_idx:] + compare[:first_idx]

# 둘 중 하나 맞으면 good puzzle
if sequence == new_list1 or sequence == new_list2:
    print("good puzzle")
else:
    print("bad puzzle")
