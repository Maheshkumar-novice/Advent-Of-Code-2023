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


map = {}
def adjacent_indices_have_symbol(adjacent_indices, array, number):#
    for row, column in adjacent_indices:
        try:
            if array[row][column] != '.' and not array[row][column].isdigit():
                if array[row][column] == '*':
                    if (row, column) in map:
                        map[(row, column)].append(int(number))
                    else:
                        map[(row, column)] = [int(number)]
                return True
        except Exception as e:
            ...
    return False
    


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
                if adjacent_indices_have_symbol(adjacent_indices, array, number):
                    ...
                number = ''
                adjacent_indices = []

    for key, value in map.items():
        if len(value) == 2:
            print(value, value[0] * value[-1])
            total += (value[0] * value[-1])

    print(total)