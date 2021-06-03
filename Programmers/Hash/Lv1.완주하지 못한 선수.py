from collections import Counter


def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

'''
collection 라이브러리 사용
일반 dict는 빼기 불가,
counter를 사용하면 key, value로 되고...카운터 객체이므로 빼기 가능
마지막 리스트로 변환 후 0번째 출력--> 탈락자는 한명이다
'''