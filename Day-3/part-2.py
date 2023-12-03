def fill_adjacent_indices(row, column, adjacent_indices):
    # TOP
    if row - 1 >= 0:
        adjacent_indices.append([row - 1, column])
    
    # BOTTOM
    adjacent_indices.append([row + 1, column])

    # LEFT
    if column - 1 >= 0:
        adjacent_indices.append([row, column - 1])

    # RIGHT
    adjacent_indices.append([row, column + 1])

    # TR_DIAG - row -1, column + 1
    if row - 1 >= 0:
        adjacent_indices.append([row - 1, column + 1])

    # TL_DIAG - row - 1, column - 1
    if row - 1 >= 0:
        adjacent_indices.append([row - 1, column - 1])

    # BR_DIAG - row + 1, column + 1
    adjacent_indices.append([row + 1, column + 1])

    # BL_DIAG - row + 1, column - 1
    if column - 1 >= 0:
        adjacent_indices.append([row + 1, column - 1])

    return adjacent_indices


stars = {}
def adjacent_numbers_of_stars(adjacent_indices, array, number):
    for row, column in adjacent_indices:
        try:
            if array[row][column] != '.' and not array[row][column].isdigit():
                if array[row][column] == '*':
                    if (row, column) in stars:
                        stars[(row, column)]['is_updated_twice'] = True
                        stars[(row, column)]['value'] = int(number) * stars[(row, column)]
                    else:
                        stars[(row, column)] = {'is_updated_twice': False, 'value': int(number)}
                    print(stars)
        except Exception as e:
            ...
    return stars
    


with open('input.txt', 'r') as f:
    array = []
    for line in f:
        array.append(list(line.strip()))

    total = 0
    number = ''
    adjacent_indices = []

    for row, line in enumerate(array):
        for column, char in enumerate(line):
            if char.isdigit():
                number += char
                fill_adjacent_indices(row, column, adjacent_indices)
            else:
                adjacent_numbers_of_stars(adjacent_indices, array, number)
                number = ''


    for key, value in stars.items():
        if 'is_updated_twice' in value and value['is_updated_twice']:
            total += value['value']
            print(value)

    print(total)