from collections import defaultdict

card_count_map = defaultdict(int)

with open('input.txt', 'r') as f:
    total = 0

    for line in f:
        card_number, numbers = line.strip().split(':')
        card_number = int(card_number.split()[-1])
        card_count_map[card_number] += 1

        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = set(winning_numbers.strip().split())
        my_numbers = set(my_numbers.strip().split())

        intersection = winning_numbers.intersection(my_numbers)

        for i in range(1, len(intersection) + 1):
            card_count_map[card_number + i] += card_count_map[card_number]

    print(sum(card_count_map.values()))