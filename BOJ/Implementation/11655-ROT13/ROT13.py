import sys

input = sys.stdin.readline

sentence = list(input().rstrip())

result = []
for x in sentence:

    if x.isupper():
        if ord(x) + 13 <= 90:
            result.append(chr(ord(x) + 13))
        else:
            result.append(chr(ord(x) - 13))
    elif x.islower():
        if ord(x) + 13 <= 122:
            result.append(chr(ord(x) + 13))
        else:
            result.append(chr(ord(x) - 13))
    else:
        result.append(x)

for x in result:
    print(x, end='')
