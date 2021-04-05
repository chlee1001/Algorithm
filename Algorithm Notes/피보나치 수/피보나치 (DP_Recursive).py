import sys

input = sys.stdin.readline
fibo = [-1] * 99


def fibo_dp(n):
    if n <= 1:
        return n
    elif fibo[n] != -1:
        return fibo[n]
    else:
        fibo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return fibo[n]


N = int(input())
print(fibo_dp(N))

"""
시간 복잡도는 O(N)입니다.
"""
