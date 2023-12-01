import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

s = 0
for line in lines:
    f = ''.join(x for x in line if x.isdigit())
    s += int(f[0] + f[-1])

print("Sum = " + str(s))
