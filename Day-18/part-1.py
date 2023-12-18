from itertools import pairwise

with open('input.txt', 'r') as f:
    updaters = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    points, point = [], (0, -1)
    for line in f:
        direction, steps, _ = line.split()
        updater = updaters[direction]
        for i in range(int(steps)):
            point = ((point[0] + updater[0]), (point[1] + updater[1]))
            points.append(point)
    
    shoelace = 0
    for i, j in pairwise(points):
        shoelace += ((i[0] * j[1]) - (i[1] * j[0]))
    
    print(abs(shoelace) // 2 + len(points) // 2 + 1)
