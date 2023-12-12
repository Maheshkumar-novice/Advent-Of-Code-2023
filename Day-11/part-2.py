import numpy as np
from itertools import combinations
import re

with open('input.txt', 'r') as f:
    file_content = f.read()
    data = file_content.splitlines()

    hash_count = len(re.findall(r'#', file_content))
    combos = list(combinations(range(1, hash_count + 1), r=2))

    rows_to_duplicate = []
    for idx, i in enumerate(data):
        data[idx] = list(i)

        if all(i == '.' for i in i):
            rows_to_duplicate.append((idx, list(i)))
    
    index = 0
    for i, row_value in rows_to_duplicate:
        data.insert(i + index + 1, ['X'] + row_value[1:])
        index += 1

   
    data = np.transpose(data).tolist()

    rows_to_duplicate = []
    for idx, i in enumerate(data):
        if all(i == '.' for i in i):
            rows_to_duplicate.append((idx, i))

    index = 0
    for i, row_value in rows_to_duplicate:
        data.insert(i + index + 1, ['X'] + row_value[1:])
        index += 1

    data = np.transpose(data).tolist()

    data_map = {}
    count = 1
    
    temp_idx = -1
    jdx_row = data[0]
    for idx, i in enumerate(data):
        if i[0] == 'X':
            temp_idx += 9_99_999
        else:
            temp_idx += 1

        temp_jdx = -1
        for jdx, j in enumerate(i):
            if jdx_row[jdx] == 'X':
                temp_jdx += 9_99_999
            else:
                temp_jdx += 1

            if j == '#':
                data[idx][jdx] = str(count)
                data_map[count] = (temp_idx, temp_jdx)
                count += 1
        idx += 1

    total = 0
    for c in combos:
        start, end = c
        x1, y1 = data_map[start]
        x2, y2 = data_map[end]

        manhattan = abs(x1 - x2) + abs(y1 - y2)
        total += manhattan

    print(total)