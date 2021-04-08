def trapping_rain(buildings):
    max_height = max(buildings)
    start_point = False
    current_height = 0
    total = 0

    for i in range(len(buildings) - 1):  # 마지막은 스킵
        if start_point == 0 and buildings[i] > 0:
            start_point = 1
            current_height = buildings[i]
        else:
            if buildings[i] == max_height:
                continue

            if buildings[i] < current_height:
                total += current_height - buildings[i]
            else:
                current_height = buildings[i]

    return total


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
