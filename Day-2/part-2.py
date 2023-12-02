import re

total = 0
with open('input.txt', 'r') as f:
    for line in f:
        game  = sum(int(i) for i in re.findall(r'Game (\d+):', line))
        red   = max(int(i) for i in re.findall(r'\d+ (?=red)', line))
        blue  = max(int(i) for i in re.findall(r'\d+ (?=blue)', line))
        green = max(int(i) for i in re.findall(r'\d+ (?=green)', line))

        total += red * blue * green

    print(total)