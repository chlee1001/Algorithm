import sys

input = sys.stdin.readline

A, B = map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

AB = set_A - set_B
BA = set_B - set_A

print(len(AB) + len(BA))
