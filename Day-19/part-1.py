import re
import operator

with open('input.txt', 'r') as f:
    operator_map = {
        '>': operator.gt,
        '<': operator.lt
    }
    instructions = {}
    for line in f:
        if line == '\n':
            break

        matches = re.match(r'(\w+){((\w+[><]\d+:\w+,)+(\w+))}', line).groups()
        key, instruction, *_ = matches
        instruction = instruction.split(',')
        instructions[key] = instruction
    
    def exec_instruction(line_val_map, instruction='in'):
        steps = iter(instructions[instruction])
        while True:
            step = next(steps).split(':')
            match step:
                case condition, instruction:
                    key = line_val_map[condition[0]]
                    op = operator_map[condition[1]]
                    value = int(condition[2:])
                    if op(key, value):
                        if instruction == 'A':
                            return 1
                        elif instruction == 'R':
                            return 0
                        else:
                            return exec_instruction(line_val_map, instruction)
                case instruction:
                    instruction = instruction[0]
                    if instruction == 'A':
                        return 1
                    elif instruction == 'R':
                        return 0
                    else:
                        return exec_instruction(line_val_map, instruction)

    total = 0
    for line in f:
        line = line.strip()[1:-1].split(',')
        line_val_map = {}
        for val in line:
            a, b = val.split('=')
            line_val_map[a] = int(b)

        is_accepted = exec_instruction(line_val_map)
        if is_accepted:
            total += sum(line_val_map.values())

    print(total)