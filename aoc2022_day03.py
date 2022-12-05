from aocd import data

# Part 1

common = [set(row[0:(len(row) // 2)]).intersection(set(row[(len(row)//2):])) for row in data.split('\n')]

# check we haven't done anything wrong
for commonitems in common:
    assert len(commonitems)==1

charnums = [ord(s.pop()) for s in common]
# A=65, Z=90, a=97, z=122
total = sum([i - 38 if i <= 90 else i - 96 for i in charnums])
print(f"Part 1: {total}")

# Part 2

rows = data.split('\n')
charnums = []
for group_idx in range(0, len(rows), 3):
    group = rows[group_idx:group_idx+3]
    common = set.intersection(*(set(elf) for elf in group))
    charnums.append(ord(common.pop()))
total2 = sum([i - 38 if i <= 90 else i - 96 for i in charnums])
print(f"Part 2: {total2}")

