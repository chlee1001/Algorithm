def solution(phone_book):
    answer = True
    phone_book.sort()
    for phone_num1, phone_num2 in zip(phone_book, phone_book[1:]):
        if phone_num2[:len(phone_num1)] == phone_num1:
            return False
    return answer


print(solution(["119", "97674223", "1195524421"]))  # false
print(solution(["123", "456", "789"]))  # true
print(solution(["12", "123", "1235", "567", "88"]))  # false
print(solution(["1235", "123", "12348", "012"]))  # false
