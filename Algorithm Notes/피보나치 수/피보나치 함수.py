import sys

input = sys.stdin.readline

n = int(input())

fibo_memo = [-1] * 99


def fibo_dynamic(n):
    if 0 < n <= 2:
        return 1
    elif n == 0:
        return 0
    if fibo_memo[n] != -1:
        return fibo_memo[n]
    fibo_memo[n] = fibo_dynamic(n - 1) + fibo_dynamic(n - 2)
    return fibo_memo[n]


print(fibo_dynamic(n))
