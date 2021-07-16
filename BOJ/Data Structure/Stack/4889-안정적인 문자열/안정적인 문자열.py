import math
import sys

input = sys.stdin.readline
i = 0
while True:
    i += 1
    input_string = list(input().rstrip())

    if input_string[0] == '-':
        break
    else:
        open_bracket = []
        close_bracket = []
        for x in input_string:
            if x == '{':
                open_bracket.append(x)
            elif x == '}':
                if open_bracket:
                    open_bracket.pop()
                else:
                    close_bracket.append(x)

        count = math.ceil(len(open_bracket) / 2) + math.ceil(len(close_bracket) / 2)
        print(f"{i}. {count}")
