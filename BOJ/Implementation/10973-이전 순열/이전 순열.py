import sys

input = sys.stdin.readline

N = int(input())
compare_list = list(map(int, input().split()))


i, j, k = [len(compare_list) - 1 for _ in range(3)]  # 맨 뒤부터...
while i > 0 and compare_list[i - 1] <= compare_list[i]:  # 맨 뒤부터 내림차순... 즉 오름차순일 경우
    i -= 1

if not i:  # 이전 순열이 없을 경우
    print(-1)
    exit(0)

while compare_list[i - 1] <= compare_list[j]:
    j -= 1
compare_list[i - 1], compare_list[j] = compare_list[j], compare_list[i - 1]

while i < k:
    compare_list[i], compare_list[k] = compare_list[k], compare_list[i]
    i += 1
    k -= 1

print(*compare_list)