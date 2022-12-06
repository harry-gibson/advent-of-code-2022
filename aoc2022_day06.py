from collections import deque

from aocd import data

d = deque(data[:4], maxlen=4)

for i, c in enumerate(data[4:]):
    if len(set(d)) == 4:
        print(i + 4)
        break
    d.append(c)

d = deque(data[:14], maxlen=14)

for i, c in enumerate(data[14:]):
    if len(set(d)) == 14:
        print(i + 14)
        break
    d.append(c)