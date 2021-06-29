import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = []


def binary_search(arr, x):
    k = bisect_left(arr, x)
    if k >= len(arr):
        arr.append(x)
    else:
        arr[k] = x
    return arr


for num in num_list:
    dp = binary_search(dp, num)

print(len(dp))
