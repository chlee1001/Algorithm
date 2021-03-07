import sys

input = sys.stdin.readline

a = int(input())
b = int(input())

c = a * (b % 10)
d = a * (b % 100 // 10)
e = a * (b // 100)
f = a * b

print(f"{c}\n{d}\n{e}\n{f}")
