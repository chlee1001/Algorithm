import sys

input = sys.stdin.readline


def isPalindrome(value):
    for i in range(len(value)):
        if value[i] != value[len(value) - 1 - i]:
            return 0
    return 1


while True:
    num = int(input())
    if not num:
        break
    else:
        arr = list(str(num))
        if isPalindrome(arr):
            print('yes')
        else:
            print('no')
