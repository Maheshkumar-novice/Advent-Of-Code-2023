from collections import deque

PIPE_MATCH_MAP = {
    '|': {
        'top': {'|', '7', 'F'},
        'bottom': {'L', 'J', '|'},
        'right': {},
        'left': {}
    },
    '-': {
        'top': {},
        'bottom': {},
        'right': {'7', 'J', '-'},
        'left': {'F', 'L', '-'}
    },
    'L': {
        'top': {'7', 'F', '|'},
        'bottom': {},
        'right': {'-', 'J', '7'},
        'left': {}
    },
    'J': {
        'top': {'|', 'F', '7'},
        'bottom': {},
        'right': {},
        'left': {'-', 'F', 'L'}
    },
    '7': {
        'top': {},
        'bottom': {'J', '|', 'L'},
        'right': {},
        'left': {'-', 'F', 'L'}
    },
    'F': {
        'top': {},
        'bottom': {'|', 'L', 'J'},
        'right': {'-', 'J', '7'},
        'left': {}
    }
}


def validate_top(top): return top[0] >= 0 and top[1] >= 0

def validate_bottom(bottom, b_max): return bottom[0] >=0 and bottom[1] >= 0 and bottom[0] < b_max

def validate_right(right, r_max): return right[0] >= 0 and right[1] >= 0 and right[1] < r_max

def validate_left(left): return left[0] >= 0 and left[1] >= 0

def get_connections(coords, data):
    r_max = len(data[0])
    b_max = len(data)


    top = (coords[0] - 1, coords[1])
    bottom = (coords[0] + 1, coords[1])
    right = (coords[0], coords[1] + 1)
    left = (coords[0], coords[1] - 1)


    if not validate_top(top):
        top = None

    if not validate_bottom(bottom, b_max):
        bottom = None

    if not validate_right(right, r_max):
        right = None

    if not validate_left(left):
        left = None

    return top, bottom, right, left



def has_connection(coords, data, connections=[], count=False):
    top, bottom, right, left = get_connections(coords, data) if not connections else connections

    symbol = data[coords[0]][coords[1]]
    if symbol == '.' or symbol == 'O' and count == False:
        return None, None, None, None  
    elif symbol == '.' and count:
        return False

    top_r = None
    if top:
        top_r = data[top[0]][top[1]] in PIPE_MATCH_MAP[symbol]['top']

    bottom_r = None
    if bottom:
        bottom_r = data[bottom[0]][bottom[1]] in PIPE_MATCH_MAP[symbol]['bottom']

    right_r = None
    if right:
        right_r = data[right[0]][right[1]] in PIPE_MATCH_MAP[symbol]['right']

    left_r = None
    if left:
        left_r = data[left[0]][left[1]] in PIPE_MATCH_MAP[symbol]['left']

   
    counter = 0
    for i in [top_r, bottom_r, right_r, left_r]:
        if i:
            counter += 1

    if count:
        return counter == 2
    else:
        if counter != 2:
            return None, None, None, None
        val = []
        if top_r:
            val.append(top)
        if bottom_r:
            val.append(bottom)
        if right_r:
            val.append(right)
        if left_r:
            val.append(left)
        return val


with open('input.txt', 'r') as f:
    import re
    fc = f.read()
    rei = re.search(r'S', fc)
    s_index = rei.span()[0]

    fcl = fc.splitlines()
    rl = len(fcl[0])
    cl = len(fcl)

    s_index = (s_index // rl,s_index - ((s_index// rl) * (rl + 1)))

    data = fc.splitlines()

    for idx, i in enumerate(data):
       data[idx] = list(i)
    
    s_index = (24, 93)

    for i in ['|', '-', 'F', '7', 'J', 'L']:
        data[s_index[0]][s_index[1]] = i
        r = has_connection(s_index, data, count=True)

        if r:
            break

    queue = deque()
    queue.append(s_index)
    visited = {}
    parent_count = {s_index: 0}
    while len(queue) != 0:
        pipe = queue.popleft()

        if pipe in visited:
            continue

        if data[pipe[0]][pipe[1]] == '.':
            continue
        
        connections = get_connections(pipe, data)
        
        for i in has_connection(pipe, data, connections=connections):
            if i and i not in visited:
                queue.append(i)
                parent_count[i] = parent_count[pipe] + 1
        visited[pipe] = True

    total = 0
    for idx, i in enumerate(data):
        inside = False
        wall = None
        for jdx, j in enumerate(i):
            if (idx, jdx) in visited:
                pipe = data[idx][jdx]
                if pipe == '|' or (wall == 'F' and pipe == 'J') or (wall == 'L' and pipe == '7'):
                    inside = not inside
                elif pipe  in 'FL':
                    wall = pipe
            elif inside:
                total += 1
    print(total)
