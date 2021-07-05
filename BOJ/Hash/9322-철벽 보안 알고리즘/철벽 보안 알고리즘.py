import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    first_public_key = list(input().split())
    second_public_key = list(input().split())
    cipher_text = list(input().split())

    rule = []
    for i in range(N):
        rule.append(second_public_key.index(first_public_key[i]))

    for i in rule:
        print(cipher_text[i], end=' ')
