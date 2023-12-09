from itertools import pairwise

with open('input.txt', 'r') as f:
    total = 0
    for line in f.read().splitlines():
        flag = False
        numbers = line.split()
        final_values =[int(numbers[0])]
        while not flag:
            is_non_zero_found = False
            final_value = -1
            next_numbers = []
            first_flag = True
            for x, y in pairwise(numbers):
                x = int(x)
                y = int(y)

                diff = y - x

                if diff != 0:
                    is_non_zero_found = True

                next_numbers.append(diff)
                
                if first_flag:
                    final_value = diff
                    first_flag = False
            
            numbers = next_numbers
            final_values.append(final_value)
            if not is_non_zero_found:
                flag = True
        result = 0
        for y in (final_values[::-1]):
            result = y - result
        total += result

    print(total)
