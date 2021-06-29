def solution(brown, yellow):
    answer = []
    carpet = brown + yellow
    for i in range(1, carpet + 1):
        col = i
        row = carpet / col

        if col >= row:
            if (col - 2) * (row - 2) == yellow:
                answer.append(col)
                answer.append(int(row))
                break

    return answer


print(solution(10, 2))
