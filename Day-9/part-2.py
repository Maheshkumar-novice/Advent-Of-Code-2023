from itertools import pairwise


with open('input.txt', 'r') as f:
    total = 0
    
    for line in f.read().splitlines():
        loop_cotinue_flag = False
        numbers = list(map(int, line.split()))
        start_of_the_sequence_values =[numbers[0]]

        while not loop_cotinue_flag:
            any_none_zero_value_found = False
            next_sequence_numbers = []

            for x, y in pairwise(numbers):
                diff = y - x

                if diff != 0:
                    any_none_zero_value_found = True

                next_sequence_numbers.append(diff)
            
            numbers = next_sequence_numbers
            start_of_the_sequence_values.append(numbers[0])

            if not any_none_zero_value_found:
                loop_cotinue_flag = True

        result = 0
        for y in (start_of_the_sequence_values[::-1]):
            result = y - result

        total += result

    print(total)
