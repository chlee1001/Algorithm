import sys

input = sys.stdin.readline


def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


N = int(input())
print(fibo(N))

""" 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됩니다. (중복되는 부분 문제) >> 비효율적
O(2^N) >> f(30)을 계산하기 위해서는 약 10억가량의 연산을 수행해야합니다.
피보나치 수열은 중복되는 부분 문제로 효율적인 해법은 다이나믹프로그래밍을 사용하는 것이다."""