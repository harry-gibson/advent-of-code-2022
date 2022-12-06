from collections import deque

from aocd import data


def day_06(message, markerlen):
    d = deque(message[:markerlen], maxlen=markerlen)
    for i, c in enumerate(message[markerlen:]):
        if len(set(d)) == markerlen: return i + markerlen
        d.append(c)

print(f"Part 1: {day_06(data, 4)}")
print(f"Part 2: {day_06(data, 14)}")