import re

with open('input.txt', 'r') as f:
    instructions, total, results = {}, 0, []
    instructions['R'] = 'R'
    instructions['A'] = 'A'

    def exec_instruction(line_val_map, instruction): 
        match instruction:
            case 'A':
                results.append(line_val_map)
                return
            case 'R':
                return
     
        instruction = instruction[::-1]
        step = instruction.pop().split(':')

        match step:
            case [condition, next_instruction]:
                operator = condition[1]
                line_val = condition[0]
                combos = line_val_map[line_val]
                value = int(condition[2:])

                if operator == '<':
                    split_1_map = line_val_map.copy()
                    split_1_combos = range(combos.start, value - 1)
                    split_1_map[line_val] = split_1_combos
                    exec_instruction(split_1_map, instructions[next_instruction])

                    split_2_map = line_val_map.copy()
                    split_2_combos = range(value, combos.stop)
                    split_2_map[line_val] = split_2_combos
                    exec_instruction(split_2_map, instruction[::-1].copy())
                if operator == '>':
                    split_1_map = line_val_map.copy()
                    split_1_combos = range(value + 1, combos.stop)
                    split_1_map[line_val] = split_1_combos
                    exec_instruction(split_1_map, instructions[next_instruction])

                    split_2_map = line_val_map.copy()
                    split_2_combos = range(combos.start, value)
                    split_2_map[line_val] = split_2_combos
                    exec_instruction(split_2_map, instruction[::-1].copy())
            case [next_instruction]:
                exec_instruction(line_val_map, instructions[next_instruction])

    for line in f:
        if line == '\n':
            break

        key, instruction, *_  = re.match(r'(\w+){((\w+[><]\d+:\w+,)+(\w+))}', line).groups()
        instructions[key] = instruction.split(',')

    line_val_map = {
        'x': range(1, 4000),
        'm': range(1, 4000),
        'a': range(1, 4000),
        's': range(1, 4000)
    }
    
    exec_instruction(line_val_map, instructions['in'])

    for result in results:
        temp = 1
        for line_val in result.values():
            temp *= ((line_val.stop - line_val.start) + 1)
        total += temp

    print(total)