test_case = int(input())
ans_list = [1, 2, 4]

for i in range(3, 11):
    ans_list.append(ans_list[i - 1] + ans_list[i - 2] + ans_list[i - 3])

for _ in range(test_case):
    n = int(input())
    print(ans_list[n - 1])
