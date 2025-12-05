with open("input", "r") as f:
    lines = f.read().splitlines()

ranges = []
ids = []

for line in lines:
    if '-' in line:
        l, u = line.split('-')
        ranges.append([int(l),int(u)])
    elif line:
        ids.append(int(line))

ranges.sort()
merged = [ranges[0]]

for curr_l, curr_u in ranges[1:]:
    last_l, last_u = merged[-1]

    if curr_l > last_u:
        merged.append([curr_l, curr_u])
    else:
        merged[-1][1] = max(last_u, curr_u)

fresh = 0
for l, u in merged:
    length = u - l + 1
    fresh = fresh + length
    
print(fresh)
