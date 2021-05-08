import sys

input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

height_sum = sum(dwarfs)
delete_element1 = 0
delete_element2 = 0

for i in range(9):
    for j in range(i + 1, 9):
        if height_sum - (dwarfs[i] + dwarfs[j]) == 100:
            delete_element1 = dwarfs[i]
            delete_element2 = dwarfs[j]
            break

for dwarf in dwarfs:
    if dwarf == delete_element1 or dwarf == delete_element2:
        continue
    else:
        print(dwarf)
