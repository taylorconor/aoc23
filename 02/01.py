import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

s = 0
for line in lines:
    num = re.search("^Game ([0-9]+): ", line)[1]
    groups = re.findall("(?:([0-9]+) ([a-z]+), )?(?:([0-9]+) ([a-z]+), )?([0-9]+) ([a-z]+)", line)
    valid = True
    for group in groups:
        m = {'red': 0, 'green': 0, 'blue': 0}
        for item in group:
            if item.isdigit():
                i = int(item)
            elif len(item):
                m[item] += i
        if m['red'] > 12 or m['green'] > 13 or m['blue'] > 14:
            valid = False
    if valid:
        s += int(num)

print("Sum = " + str(s))
