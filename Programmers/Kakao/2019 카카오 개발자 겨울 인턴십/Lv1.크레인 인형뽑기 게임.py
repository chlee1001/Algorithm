def solution(board, moves):
    N = len(board)  # 보드의 길이
    answer = 0
    basket = []
    for move in moves:
        for i in range(N):
            if board[i][move - 1] > 0:  # Move별로 맨 위에 있는 인형을 바구니에 넣고, 빈칸으로 전환
                basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

        if len(basket) > 1:  # 바구니가 2개이상일 때부터
            if basket[-1] == basket[-2]:  # 가장 최신에 들어온 것과 그 전에 들어온 것이 같으면 두개 삭제
                basket.pop()
                basket.pop()
                answer += 2

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
