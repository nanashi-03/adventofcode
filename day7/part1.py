lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

splits = 0

source = lines[0].find('S')

beams = set([source])

for line in lines[1:]:
    next = set()
    
    for beam in beams:
        if line[beam] == '.':
            next.add(beam)
        elif line[beam] == '^':
            next.add(beam + 1)
            next.add(beam - 1)
            splits = splits + 1

    beams = next

print(splits)
