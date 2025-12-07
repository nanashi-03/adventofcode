lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

source = lines[0].find('S')
beams = set([source])
c = {source : 1}

for line in lines[1:]:
    next = set()
    newc = dict()
    
    for beam in beams:
        if line[beam] == '.':
            next.add(beam)
            newc[beam] = newc.get(beam, 0) + c[beam]
        elif line[beam] == '^':
            left = beam - 1
            right = beam + 1

            next.add(left)
            newc[left] = newc.get(left, 0) + c[beam]

            next.add(right)
            newc[right] = newc.get(right, 0) + c[beam]

    beams = next
    c = newc

total = 0

for value in c.values():
    total = total + value

print(total)
