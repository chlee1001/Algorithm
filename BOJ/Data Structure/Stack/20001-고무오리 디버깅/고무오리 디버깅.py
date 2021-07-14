import sys

input = sys.stdin.readline

start = input().rstrip()

question = []
while True:
    input_string = input().rstrip()
    if input_string == '고무오리 디버깅 끝':
        break
    else:
        if input_string == '문제':
            question.append(0)
        elif input_string == '고무오리':
            if question:
                question.pop()
            else:
                question.append(0)
                question.append(0)

if question:
    print("힝구")
else:
    print("고무오리야 사랑해")
