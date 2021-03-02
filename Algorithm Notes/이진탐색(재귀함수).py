# 이진 탐색 소스코드 구현 (재귀함수)
def binary_search(array, target, start, end):
    if start > end:  # 데이터가 존재X
        return None
    mid = (start + end) // 2
    # target을 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return 1
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


array_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = [5, -1]
for i in range(2):
    if binary_search(array_list, target[i], 0, len(array_list) - 1) == 1:
        print(f"{target[i]}는 존재합니다.")
    else:
        print(f"{target[i]}는 존재하지 않습니다.")
