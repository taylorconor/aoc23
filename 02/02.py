import os, re, math

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

s = 0
for line in lines:
    num = re.search("^Game ([0-9]+): ", line)[1]
    groups = re.findall("(?:([0-9]+) ([a-z]+), )?(?:([0-9]+) ([a-z]+), )?([0-9]+) ([a-z]+)", line)
    mm = {'red': 0, 'green': 0, 'blue': 0}
    for group in groups:
        m = {'red': 0, 'green': 0, 'blue': 0}
        for item in group:
            if item.isdigit():
                i = int(item)
            elif len(item):
                m[item] += i
        mm = {k: max(m[k], v) for k, v in mm.items()}
    s += math.prod(mm.values())

print("Sum = " + str(s))
