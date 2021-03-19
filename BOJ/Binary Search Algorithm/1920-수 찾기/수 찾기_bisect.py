import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))


def binary_search(arr, x):
    temp = bisect_left(arr, x)
    return temp < len(arr) and arr[temp] == x


A.sort()
for i in B:
    if binary_search(A, i):
        print(1)
    else:
        print(0)
