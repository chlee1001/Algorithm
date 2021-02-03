# h (시) 입력받기
h = int(input())

count = 0
for hh in range(h + 1):
    for mm in range(60):
        for ss in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(hh) + str(mm) + str(ss):
                count += 1

print(count)
