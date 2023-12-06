with open('input.txt', 'r') as f:
    f = f.read().splitlines()
    time = int(''.join(f[0].split()[1::]))
    distance = int(''.join(f[1].split()[1::]))

    time_distance_map = {time: distance}
    print(time_distance_map)

    total = 1
    for time in time_distance_map.keys():
        start = 0
        remaining = time
        larger_counts_count = 0
        while remaining > 0:
            if start * remaining > time_distance_map[time]:
                larger_counts_count += 1
            start += 1
            remaining -= 1
        total *= larger_counts_count if larger_counts_count > 0 else 1
    print(total)
