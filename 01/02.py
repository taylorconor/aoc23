import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

values = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

ss = 0
for line in lines:
    s = ""
    for i, c in enumerate(line):
        if c.isdigit():
            s += c
        for n in values:
            if line[i:].startswith(n):
                s += values[n]
    ss += int(s[0] + s[-1])

print("Sum = " + str(ss))
