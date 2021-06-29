from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    while queue:
        idx, total = queue.popleft()

        if idx == len(numbers):
            if total == target:
                answer += 1
        else:
            num = numbers[idx]
            queue.append((idx + 1, total + num))
            queue.append((idx + 1, total - num))
    return answer


print(solution([1, 1, 1, 1, 1], 3))
