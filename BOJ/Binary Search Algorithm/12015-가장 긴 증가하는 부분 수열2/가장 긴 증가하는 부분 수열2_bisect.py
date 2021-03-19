import sys
from bisect import bisect_left  # 이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = []

for num in num_list:
    k = bisect_left(dp, num)  # 자신이 들어갈 위치 K
    if k >= len(dp):  # num이 가장 큰 숫자라면
        dp.append(num)
    else:
        dp[k] = num  # 자신보다 큰 수 중 최솟값과 대체

print(len(dp))

# for i in range(N):
#     start = 0
#     end = len(dp) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if num_list[i] > dp[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     if start >= len(dp):
#         dp.append(num_list[i])
#     else:
#         dp[start] = num_list[i]
