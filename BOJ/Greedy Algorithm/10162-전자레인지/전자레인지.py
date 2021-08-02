import sys

input = sys.stdin.readline

T = int(input())

control = [300, 60, 10]
count = [0, 0, 0]
for i in range(3):
    if T >= control[i]:
        count[i] = T // control[i]
        T %= control[i]

if not T:
    print(*count)
else:
    print(-1)
