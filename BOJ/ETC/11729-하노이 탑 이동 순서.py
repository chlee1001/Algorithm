def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n - 1, a, c, b)
        move.append([a, c])
        hanoi(n - 1, b, a, c)


N = int(input())
move = []
hanoi(N, 1, 2, 3)


print(len(move))
print('\n'.join([' '.join(str(i) for i in row) for row in move]))
