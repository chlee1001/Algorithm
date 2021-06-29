import sys

input = sys.stdin.readline

k, n = map(int, input().split())

cables_list = []
for _ in range(k):
    cables_list.append(int(input()))

start = 1
end = max(cables_list)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in range(k):
        if cables_list[i] >= mid:
            total += cables_list[i] // mid

    if total < n:  # 목표보다 적을 경우 기준을 왼쪽으로...
        end = mid - 1
    else: # 목표보다 여유로울 경우, 오른쪽으로
        start = mid + 1
        result = mid

print(result)
