import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    ll = [x.strip().split(':')[1].split('|') for x in f.read().splitlines()]

s = 0
for l in ll:
    a = set()
    for m in re.findall('\d+', l[0]):
        a.add(int(m))
    b = set()
    for m in re.findall('\d+', l[1]):
        b.add(int(m))
    if len(a.intersection(b)) > 0:
        s += 2 ** (len(a.intersection(b)) - 1)

print("Sum = " + str(s))
