def solution(numbers, hand):
    number_coord = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    left_hand = (3, 0)
    right_hand = (3, 2)
    answer = ''

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = number_coord[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_hand = number_coord[number]
        elif number in [2, 5, 8, 0]:
            # 다음 pos의 좌료와 현재 양손의 좌표사이의 거리 구하기
            next_x, next_y = number_coord[number]
            left_x, left_y = left_hand
            right_x, right_y = right_hand
            # abs(x_h - x_n) + abs(y_h - y_n)

            left_distance = abs(next_x - left_x) + abs(next_y - left_y)
            right_distance = abs(next_x - right_x) + abs(next_y - right_y)
            if left_distance < right_distance:
                answer += 'L'
                left_hand = number_coord[number]
            elif left_distance == right_distance:
                if hand == 'right':
                    answer += 'R'
                    right_hand = number_coord[number]
                else:
                    answer += 'L'
                    left_hand = number_coord[number]
            else:
                answer += 'R'
                right_hand = number_coord[number]
    return answer


# 테스트 예시
t1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]  # right
t2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]  # left
t3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # right

print(solution(t3, 'right'))

'''
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
'''
