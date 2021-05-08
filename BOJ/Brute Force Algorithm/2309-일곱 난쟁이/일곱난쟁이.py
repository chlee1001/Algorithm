import sys
from itertools import combinations

input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

nPr = combinations(dwarfs, 7)

temp = []
for case in list(nPr):
    if sum(case) == 100:
        temp = case
        break
for x in temp:
    print(x)
