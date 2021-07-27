import sys

input = sys.stdin.readline
oct_num = list(input().rstrip())
dec_num = 0
bin_num = []

for i in range(len(oct_num)):
    num = int(oct_num[-1 - i])
    num *= 8 ** i
    dec_num += num

while dec_num > 1:
    temp = dec_num % 2
    dec_num //= 2
    bin_num.append(temp)
bin_num.append(1)

for i in range(len(bin_num) - 1, -1, -1):
    print(bin_num[i], end='')

# print(bin(int(input(), 8))[2:])
