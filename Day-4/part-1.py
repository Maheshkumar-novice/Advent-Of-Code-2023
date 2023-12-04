with open('input.txt', 'r') as f:
    total = 0

    for line in f:
        _, numbers = line.strip().split(':')

        winning_numbers, my_numbers = numbers.split('|')

        winning_numbers = set(winning_numbers.strip().split())
        my_numbers = set(my_numbers.strip().split())

        intersection = winning_numbers.intersection(my_numbers)

        card_value = 2 ** (len(intersection) - 1) if len(intersection) > 0 else 0

        total += card_value

    print(total)
