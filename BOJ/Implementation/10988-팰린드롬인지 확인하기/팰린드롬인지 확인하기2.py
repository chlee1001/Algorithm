import sys

input = sys.stdin.readline

input_string = list(input().rstrip())
palindrome = 1
for i in range(len(input_string) // 2):
    if input_string[i] != input_string[len(input_string) - 1 - i]:
        palindrome = 0

if palindrome:
    print(1)
else:
    print(0)
