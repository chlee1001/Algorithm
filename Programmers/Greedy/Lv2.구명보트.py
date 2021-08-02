def solution(people, limit):
    people_list = sorted(people)
    answer = 0

    head, tail = 0, len(people_list) - 1
    while head <= tail:
        if people_list[head] + people_list[tail] <= limit:  # 가장 가벼운 사람과 가장 무거운 사람이 같이 타면, 같이 보내기
            head += 1
            tail -= 1
        else:  # 가장 가벼운 사람과 가장 무거운 사람이 같이 못타는 경우, 가장 무거운 사람 혼자 보내기
            tail -= 1
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3
