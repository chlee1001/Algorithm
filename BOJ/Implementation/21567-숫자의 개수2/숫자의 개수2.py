import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
product_value = A * B * C

split_num = list(str(product_value).rstrip())

num_dict = {}

for i in range(10):
    num_dict[i] = 0

for num in split_num:
    num_dict[int(num)] += 1

for i in range(10):
    print(num_dict[i])
