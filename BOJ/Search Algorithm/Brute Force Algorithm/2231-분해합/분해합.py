n = int(input())

for i in range(1, n + 1):
    divide_nums = list(map(int, str(i)))  # 숫자를 자리수별로 분리
    sum_num = i + sum(divide_nums)
    if sum_num == n:
        print(i)
        break

    if i == n:
        print(0)
