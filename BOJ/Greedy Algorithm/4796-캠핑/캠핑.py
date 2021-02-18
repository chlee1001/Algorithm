case_num = 0
while True:
    case_num += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    l_group = v // p
    l_remain = v % p
    result = l_group * l + min(l, l_remain)

    print(f"Case {case_num}: {result}")
