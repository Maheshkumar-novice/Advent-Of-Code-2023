from itertools import pairwise


with open('sample.txt', 'r') as f:
    total = 0

    for line in f.read().splitlines():
        loop_continue_flag = False
        numbers = list(map(int, line.split()[::-1]))
        print(numbers)
        end_of_the_sequence_value = numbers[-1]

        while not loop_continue_flag:
            any_non_zero_value_found = False
            next_sequence_numbers = []

            for x, y in pairwise(numbers):
                diff = y - x

                if diff != 0:
                    any_non_zero_value_found = True

                next_sequence_numbers.append(diff)
            
            numbers = next_sequence_numbers
            end_of_the_sequence_value += numbers[-1]

            if not any_non_zero_value_found:
                loop_continue_flag = True

        total += end_of_the_sequence_value

    print(total)
