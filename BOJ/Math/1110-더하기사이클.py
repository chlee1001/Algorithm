N = int(input())

new_num = N
result = 0
while True:
    ten = new_num // 10  # 십의 자리
    one = new_num % 10  # 일의 자리
    sum_num = (ten + one) % 10  # 자리수 합의 일의 자리

    new_num = one * 10 + sum_num

    result += 1
    if N == new_num:
        break

print(result)
