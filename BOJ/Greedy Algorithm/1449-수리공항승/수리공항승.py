import sys

input = sys.stdin.readline

N, L = map(int, input().split())

leak_list = sorted(list(map(int, input().split())))

distance = leak_list[0] + L - 0.5
count = 1
for i in range(N):
    if distance >= leak_list[i]:
        continue
    else:
        count += 1
        distance = leak_list[i] + L - 0.5
print(count)
