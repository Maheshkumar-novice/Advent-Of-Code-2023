from itertools import pairwise

with open('input.txt', 'r') as f:
    total = 0
    for line in f.read().splitlines():
        final_values = []
        flag = False
        numbers = line.split()
        final_values = int(numbers[-1])
        while not flag:
            is_non_zero_found = False
            final_value = -1
            next_numbers = []
            for x, y in pairwise(numbers):
                x = int(x)
                y = int(y)

                diff = y - x

                if diff != 0:
                    is_non_zero_found = True

                next_numbers.append(diff)
                final_value = diff
            
            numbers = next_numbers
            final_values += final_value
            if not is_non_zero_found:
                flag = True
        total += final_values

    print(total)
