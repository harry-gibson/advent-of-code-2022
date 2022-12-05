import re
from collections import defaultdict

from aocd import data

stacks, instructions = data.split('\n\n')

def parse_stacks(s):
    rows = s.split('\n')
    yard = defaultdict(list)
    #ids, pos = zip(*[(m.group(), m.start()) for m in re.finditer('\d+', rows[:-1])])
    columns = [(m.group(), m.start()) for m in re.finditer('\d+', rows[-1])]
    for row in rows[:-1][::-1]:
        for id, pos in columns:
            if row[pos] != ' ': yard[int(id)].append(row[pos])
    return yard

# PART 1

def update_cm9000(stackdict, move):
    n, fr, to = (int(i) for i in re.findall('\d+', move))
    for _ in range(n):
        crate = stackdict[fr].pop()
        stackdict[to].append(crate)
    return stackdict

yard = parse_stacks(stacks)
for row in instructions.split('\n'):
    update_cm9000(yard, row)

print('Part 1: ' + ''.join(v[-1] for v in yard.values()))

# PART 2

def update_cm9001(stackdict, move):
    n, fr, to = (int(i) for i in re.findall('\d+', move))
    stackdict[to].extend(stackdict[fr][-n:])
    stackdict[fr] = stackdict[fr][:-n]
    return stackdict

yard2 = parse_stacks(stacks)
for row in instructions.split('\n'):
    update_cm9001(yard2, row)

print('Part 2: ' + ''.join(v[-1] for v in yard2.values()))

