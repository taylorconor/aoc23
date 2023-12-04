import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    ll = [x.strip().split(':')[1].split('|') for x in f.read().splitlines()]

s = [1] * len(ll)
for i, l in enumerate(ll):
    a = set()
    for m in re.findall('\d+', l[0]):
        a.add(int(m))
    b = set()
    for m in re.findall('\d+', l[1]):
        b.add(int(m))
    for j in range(len(a.intersection(b))):
        s[i + j + 1] += s[i]

print("Sum = " + str(sum(s)))
