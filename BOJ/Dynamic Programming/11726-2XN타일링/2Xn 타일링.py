n = int(input())
result_list = [0] * 1001

result_list[1] = 1
result_list[2] = 2
for i in range(3, n + 1):
    result_list[i] = result_list[i - 1] + result_list[i - 2]

print(result_list[n] % 10007)
