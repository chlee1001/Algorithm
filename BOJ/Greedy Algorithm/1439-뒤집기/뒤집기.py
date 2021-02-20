data = input()

count0 = 0
count1 = 0

if data[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))
