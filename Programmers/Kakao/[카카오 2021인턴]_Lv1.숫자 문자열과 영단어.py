def solution(s):
    convert_table = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                     'nine': 9}

    answer = s
    for word, num in convert_table.items():
        answer = answer.replace(word, str(num))

    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution('2three45sixseven'))
print(solution('nine8sevenseven'))
print(solution('sixsevensixsevensix'))
print(solution('667676'))
