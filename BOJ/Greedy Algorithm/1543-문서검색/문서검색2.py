import sys
from collections import Counter

input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()
doc = doc.replace(word, "?")

temp = dict(Counter(list(doc)))
if '?' in temp:
    print(temp['?'])
else:
    print(0)