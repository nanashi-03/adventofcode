lines = []
for line in open("input", "r").readlines():
    lines.append(line.strip())

width = len(lines[0])+2

map = []
map.append(['.']*width)
for line in lines:
    map.append(["."] + list(line) + ["."])
map.append(['.']*width)

height = len(map)

def find_positions(map, w, h):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    positions = []
    for i in range(1, h-1):
        for j in range(1, w-1):
            vicinity = 0
            for direction in directions:
                if map[i + direction[0]][j + direction[1]] == "@":
                    vicinity = vicinity + 1

            if map[i][j] == '@' and vicinity < 4:
                positions.append((i, j))

    return positions

count = 0
pos = find_positions(map, width, height)

while True:
    c = len(pos)
    if c <= 0:
        break

    count = count + c

    for i, j in pos:
        map[i][j] = '.'

    pos = find_positions(map, width, height)

print(count)
