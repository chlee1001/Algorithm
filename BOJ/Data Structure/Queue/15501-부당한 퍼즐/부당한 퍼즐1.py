import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
compare = list(map(int, input().split()))

new_list1 = []
new_list2 = []

first_idx = compare.index(sequence[0])  # 기준점

# 순방향인 경우
start = first_idx - N
end = first_idx

for i in range(start, end):
    new_list1.append(compare[i])

# 역방향인 경우
start = first_idx
end = first_idx - N

for i in range(start, end, -1):
    new_list2.append(compare[i])

# 둘 중 하나 맞으면 good puzzle
if sequence == new_list1 or sequence == new_list2:
    print("good puzzle")
else:
    print("bad puzzle")

'''
5
1 2 3 4 5
3 4 5 1 2

6
1 2 3 4 5 6
3 2 1 6 5 4
4 5 6 1 2 3

11
11 10 9 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 10 11

'''
