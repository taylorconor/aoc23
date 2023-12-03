import os, re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    ll = [x.strip() for x in f.read().splitlines()]

s = 0
for r, l in enumerate(ll):
    for m in re.finditer('\d+', l):
        symbol = False
        for c in range(m.start(), m.end()):
            nn = [(rr, cc) for rr, cc in [(x, y) for x in (r-1, r, r+1) for y in (c-1, c, c+1)] if
                  0 <= rr < len(ll) and 0 <= cc < len(ll[rr]) and ll[rr][cc] is not None]
            for n in nn:
                if ll[n[0]][n[1]] not in set('0123456789.'):
                    symbol = True
        if symbol:
            s += int(m.group())

print("Sum = " + str(s))
