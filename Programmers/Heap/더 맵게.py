import heapq


def solution(scoville, K):
    answer = 0
    # heap = []
    # for num in scoville:
    #     heapq.heappush(heap, num)
    heapq.heapify(scoville)

    while scoville[0] < K:
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
