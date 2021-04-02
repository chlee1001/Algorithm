import sys

input = sys.stdin.readline


def power(a, b):
    if b == 1:
        return a % C
    else:
        if b % 2 == 0:  # B가 짝수일 때
            return power(a, b // 2) ** 2 % C
        else:
            return power(a, b // 2) ** 2 * a % C


A, B, C = map(int, input().split())
print(power(A, B))
