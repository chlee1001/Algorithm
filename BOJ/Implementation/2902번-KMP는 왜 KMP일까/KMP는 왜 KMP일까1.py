input_string = list(input().rstrip())
output_string = ''

for x in input_string:
    if 'A' <= x <= 'Z':
        output_string += x

print(output_string)