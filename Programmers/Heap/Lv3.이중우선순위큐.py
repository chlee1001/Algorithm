import heapq


def solution(operations):
    answer = []
    heapq.heapify(answer)
    for comm in operations:
        com, num = comm.split()
        if com == 'I':
            heapq.heappush(answer, int(num))
        elif com == 'D':
            if not answer:
                continue
            else:
                if num == '1':
                    answer.pop(answer.index(heapq.nlargest(1, answer)[0]))
                elif num == '-1':
                    heapq.heappop(answer)

    if not answer:
        return [0, 0]
    else:
        return [heapq.nlargest(1, answer)[0], answer[0]]


print(solution(["I 7", "I 5", "I -5", "D -1"]))
