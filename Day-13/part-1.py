import numpy


def get_count(data):
    for intersection_index in range(1, len(data)):
        taking = data[:intersection_index][::-1]
        remaining = data[intersection_index:]

        if all(i == j for i, j in (zip(taking, remaining))):
            return intersection_index


with open('input.txt', 'r') as f:
    total = 0
    for line in f.read().split('\n\n'):
        r_data = line.split()

        if row_wise := get_count(r_data):
            total += row_wise * 100

        d = []
        for line in r_data:
            d.append(list(line))
        c_data = numpy.transpose(d).tolist()
        c_data = [''.join(line) for line in c_data]
        column_wise = get_count(c_data)

        if column_wise := get_count(c_data):
            total += column_wise

      
    print(total)

