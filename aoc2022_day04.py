from aocd import data

#pairs = [elf.split('-') for row in data.split('\n') for elf in row.split(',') ]
pairs = [row.split(',') for row in data.split('\n')]

def parse_elf(s):
    first, last = (int(i) for i in s.split('-'))
    vals = set((range(first,last+1)))
    return vals

redundant_part1 = 0
overlaps_part2 = 0
for pair in pairs:
    s1, s2 = (parse_elf(e) for e in pair)
    if not s1.isdisjoint(s2):
        overlaps_part2 += 1
        if s1.issubset(s2) or s1.issuperset(s2):
            redundant_part1 += 1
print(redundant_part1)
print(overlaps_part2)

