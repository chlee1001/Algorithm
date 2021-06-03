from itertools import permutations
import re


def solution(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    result = []

    for op_prior in prior:
        temp = re.compile("(\D)").split('' + expression)
        for exp in op_prior:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx - 1] + [str(eval(''.join(temp[idx - 1:idx + 2])))] + temp[idx + 2:]
        result.append(abs(int(temp[0])))
    return max(result)


if __name__ == "__main__":
    expression_list = ["100-200*300-500+20", "50*6-3*2"]
    result_list = [60420, 300]

    length = len(result_list)

    for i in range(length):
        answer = solution(expression_list[i])
        if answer == result_list[i]:
            print('{}번 정답입니다.'.format(i + 1))
        else:
            print('{}번 실패입니다.'.format(i + 1))
            print('{} != {}'.format(answer, result_list[i]))
