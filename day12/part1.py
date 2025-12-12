with open("input", "r") as f:
    input = f.read().strip()

*s, regions = input.split('\n\n')
shapes = []
for shape in s:
    shapes.append(shape.count('#'))

area = 0

for line in regions.split('\n'):
    a, *counts = line.split()
    width, length = map(int, a[:-1].split('x'))

    counts = list(map(int, counts))
    
    s = 0
    for i in range(len(counts)):
        s = s + (counts[i] * shapes[i])

    area = area + (width * length >= s)

print(area)
