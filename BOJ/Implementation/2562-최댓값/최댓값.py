num_list = []
for _ in range(9):
    num_list.append(int(input()))

max = 0
position = 0
for idx, n in enumerate(num_list):
    if n > max:
        max = n
        position = idx

print(max, position + 1)
