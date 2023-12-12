import re, itertools

with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        i, matchers = line.split()
        matchers = matchers.split(',')
        mat = []
        for g in matchers:
            mat.append('#' * int(g))

        for j in itertools.product('#.', repeat=i.count('?')):
            z = list(i)
            index = 0
            for idx, m in enumerate(z):
                if m == '?':
                    z[idx] = j[index]
                    index += 1
            z = ''.join(z)
            
            if re.findall(r'#+', z) == mat:
                count += 1
    print(count)