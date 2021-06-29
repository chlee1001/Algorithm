import sys

input = sys.stdin.readline

n, m = map(int, input().split())

no_listens = []
no_watches = []

for _ in range(n):
    no_listens.append(input())
for _ in range(m):
    no_watches.append(input())


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


# no_listen에 no_watch가 있는지 확인
no_listens.sort()
no_listen_watch = []

for i in range(m):
    if binary_search(no_listens, no_watches[i], 0, n - 1) == 1:
        no_listen_watch.append(no_watches[i])

no_listen_watch.sort()
print(len(no_listen_watch))
for x in no_listen_watch:
    print(x, end="")
