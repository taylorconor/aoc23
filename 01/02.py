import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = [x.strip() for x in f.read().splitlines()]

print("02")