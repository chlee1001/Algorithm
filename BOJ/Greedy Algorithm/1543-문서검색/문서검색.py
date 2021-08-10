import sys

input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

count = 0
idx = 0

while idx <= len(doc) - len(word):
    if doc[idx:idx + len(word)] == word:
        count += 1
        idx += len(word)
    else:
        idx += 1
print(count)
