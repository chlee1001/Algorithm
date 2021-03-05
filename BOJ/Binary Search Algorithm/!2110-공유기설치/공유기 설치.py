import sys

input = sys.stdin.readline

n, c = map(int, input().split())
routers_list = []
for _ in range(n):
    routers_list.append(int(input()))

routers_list.sort()
start = 1
end = routers_list[-1] - routers_list[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = routers_list[0]
    count = 1
    for i in range(1, len(routers_list)):
        if routers_list[i] >= value + mid:
            value = routers_list[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
