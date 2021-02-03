input_data = input()
alpha = []
value = 0

# 문자를 하나씩 확인하며
for i in input_data:
    # 알파벳인 경우 알파 리스트에 삽입
    if i.isalpha():
        alpha.append(i)
    # 숫자는 따로 더하기
    else:
        value += int(i)

# 알파벳을 오름차순으로 정렬
alpha.sort()

# 정렬 된 알파벳을 결과 리스트로..
result = alpha

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))
