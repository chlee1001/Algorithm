def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

'''
탈락자는 무조건 한명
참여자 명단의 인덱스와 완주자 명단의 인덱스 값이 다르다면,
그 때, 참여자는 완주자 명단에 없으므로, 반환
----
마지막까지 인덱스 값이 같다면, 참여자 명단 마지막 사람이 완주하지 못한 사람이다.
'''
