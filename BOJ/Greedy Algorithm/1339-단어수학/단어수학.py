import sys

input = sys.stdin.readline

n = int(input())

words = []
for i in range(n):
    words.append(list(input().strip()))

alpha = [0] * 26  # A,B,C,...,X,Y,Z

for word in words:
    e = 0
    for i in word[::-1]:
        alpha[ord(i) - 65] += 10 ** e  # 문자(알파벳)을 아스키코드변환하여 alpha리스트에 자리수를 넣어줌
        e += 1

alpha.sort(reverse=True)
result = 0
t = 9
for i in range(26):
    if alpha == 0:
        break
    result += alpha[i] * t
    t -= 1

print(result)
