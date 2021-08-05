import sys

input = sys.stdin.readline

N = int(input())
seats = input().rstrip()

couples = seats.count('LL')

if couples < 2:
    print(len(seats))
else:
    print(len(seats) - couples + 1)
