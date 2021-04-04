import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
mod = 1000000
p = int(mod / 10 * 15)
fibo = [0] * p


def fibo_dp(n):
    if n <= 1:
        return n
    elif fibo[n] != 0:
        return fibo[n]
    else:
        fibo[n] = (fibo_dp(n - 1) + fibo_dp(n - 2)) % mod
        return fibo[n]


print(fibo_dp(N % p))

"""
이렇게 풀어도 가능은 하나, 
재귀를 많이 하게 되어 실제 문제에서는 오답처리가 될 수 있다. 재귀대신 반복문을 통해 푸는 걸 추천
"""
