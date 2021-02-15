num_list = list(range(1, 10_001))
remove_list = []  # 이후에 삭제할 숫자 list

for num in num_list:
    for n in str(num):
        num += int(n)  # 생성자
    remove_list.append(num)

self_num = set(num_list) - set(remove_list)
for num in sorted(self_num):
    print(num)
