import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

word_list = []
sorted_word_list = []

for _ in range(n):
    word_list.append(input())

# 중복 삭제
word_list = list(set(word_list))

# 중복을 제거한 집합으로부터 원소를 하나씩 꺼내 (단어의 길이, 단어) 튜플을 sorted_word_list 에 추가
for word in word_list:
    sorted_word_list.append((len(word), word))

# 리스트 원소들의 길이를 기준으로 리스트 정렬
sorted_word_list.sort()
for word_len, word in sorted_word_list:
    print(word)
