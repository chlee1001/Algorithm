import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
parrot = [deque(input().rstrip().split()) for _ in range(N)]

L = input().rstrip().split()
parrot_sentence = []
for word in L:
    for i in range(N):
        if parrot[i] and word == parrot[i][0]:
            parrot[i].popleft()
            parrot_sentence.append(word)
            break

# 첫 번째, L을 전부 돌았을 때, 앵무새가 들고온 문장의 단어들이 모두 소모되지 않았으면
# L이 올바른 문장이 아니라는 증거
for i in range(N):
    if parrot[i]:
        print("Impossible")
        exit()

# 두 번째, L에 앵무새가 들고 오지 않은 단어가 있는 경우
# L의 단어를 돌면서 앵무새가 들고온 단어가 있으면 다른 리스트에 넣어주고
# 마지막에 L 문장과 리스트를 비교한다.
if L != parrot_sentence:
    print("Impossible")
else:
    print("Possible")
