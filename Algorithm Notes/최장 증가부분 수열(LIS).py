"""
LIS... 최장 증가 부분 수열

기존 증가수열에 a[i]를 붙일려면, 그 중가 수열이 a[i]보다 앞에 있어야함 (j<i)
그리고 마지막 수가 a[i]보다 작아야한다. a[j]<a[i]
--> D[i]=  max(D[j]+1) // 1<=j<i, aj<ai
"""
import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):  # j<i
        if num_list[j] < num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
