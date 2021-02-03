array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 파이썬의 장점을 이용해서 짧게 작성했지만, 시간 면에서는 조금 비효율적이다.
def quick_sort(array):
    #  리스트가 하나 이하의 원소만을 담고 잇다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할 된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할 된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array1))
