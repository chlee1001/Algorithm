import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

A.sort()
for i in range(m):
    print(binary_search(A, B[i], 0, n - 1))
