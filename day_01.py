from aocd import data

elflists = data.split('\n\n')
sums = [sum([int(i) for i in elf.split('\n')]) for elf in elflists]
part1 = max(sums)

print(f"Part 1: {part1}")

print(f"Part 2: {sum(sorted(sums, reverse=True)[:3])}")