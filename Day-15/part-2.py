from collections import defaultdict

with open('input.txt', 'r') as f:
    total, boxes, focal_length_map = 0, defaultdict(list), defaultdict(int)
    
    for seq in f.read().strip().split(','):
        if '-' in seq:
            label, operation = seq.split('-')[0], '-'
        else:
            label, focal_length = seq.split('=')
            focal_length_map[label], operation = int(focal_length), '='

        label_hash = 0
        for char in label:
            label_hash += ord(char)
            label_hash *= 17
            label_hash %= 256
        
        match operation:
            case '=':
                if label not in boxes[label_hash]:
                    boxes[label_hash].append(label)
            case '-':
                if label in boxes[label_hash]:
                    boxes[label_hash].remove(label)

    for box, lenses in boxes.items():
        for idx, lens in enumerate(lenses):
            total += (box + 1) * (idx + 1) * focal_length_map[lens]
        
    print(total)
