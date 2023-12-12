import numpy as np
from itertools import combinations
import re

with open('sample.txt', 'r') as f:
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
        data.insert(i + index, row_value)
        index += 1

   
    data = np.transpose(data).tolist()

    rows_to_duplicate = []
    for idx, i in enumerate(data):
        if all(i == '.' for i in i):
            rows_to_duplicate.append((idx, i))

    index = 0
    for i, row_value in rows_to_duplicate:
        data.insert(i + index, row_value)
        index += 1


    data = np.transpose(data).tolist()

    data_map = {}
    count = 1
    for idx, i in enumerate(data):
        for jdx, j in enumerate(i):
            if j == '#':
                data[idx][jdx] = str(count)
                data_map[count] = (idx, jdx)
                count += 1

    total = 0
    for c in combos:
        start, end = c
        x1, y1 = data_map[start]
        x2, y2 = data_map[end]

        manhattan = abs(x1 - x2) + abs(y1 - y2)
        total += manhattan

    print(total)