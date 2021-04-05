import sys

input = sys.stdin.readline

N = int(input())
mod = 1000000007
fibo = {}


def fibo_dp(n):
    if n <= 1:
        return n
    elif fibo.get(n):
        return fibo[n]
    else:
        if n % 2 == 1:  # 홀수
            m = (n + 1) // 2
            temp1 = fibo_dp(m)
            temp2 = fibo_dp(m - 1)
            fibo[n] = temp1 ** 2 + temp2 ** 2
            fibo[n] %= mod
            return fibo[n]
        else:  # 짝수
            m = n // 2
            temp1 = fibo_dp(m - 1)
            temp2 = fibo_dp(m)
            fibo[n] = (2 * temp1 + temp2) * temp2
            fibo[n] %= mod
            return fibo[n]


print(fibo_dp(N))

