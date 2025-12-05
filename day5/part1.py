with open("input", "r") as f:
    lines = f.read().splitlines()

ranges = []
ids = []

for line in lines:
    if '-' in line:
        l, u = line.split('-')
        ranges.append((int(l),int(u)))
    elif line:
        ids.append(int(line))

fresh = 0

for id in ids:
    in_range = False
    for l, u in ranges:
        if l <= id <= u:
            in_range = True
            break

    if in_range:
        fresh = fresh + 1

print(fresh)
