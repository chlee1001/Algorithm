import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees_list = list(map(int, input().split()))

start = 0
end = max(trees_list)

result = 0

# 이진탐색(반복문)
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees_list:
        if tree > mid:
            total += tree - mid
    if total < m:  # 나무 길이가 부족한 경우
        end = mid - 1
    else:  # 나무 길이가 충분한 경우
        result = mid
        start = mid + 1

print(result)
