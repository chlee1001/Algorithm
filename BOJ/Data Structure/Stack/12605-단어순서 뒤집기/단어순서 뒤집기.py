import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    sentence = list(input().rstrip().split())
    result = []
    while sentence:
        result.append(sentence.pop())
    print('Case #{0}: {1}'.format(i + 1, ' '.join(result)))
