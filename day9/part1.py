with open("input", "r") as f:
    lines = f.readlines()

coordinates = []
for line in lines:
    coordinates.append(list(map(int, line.split(','))))

area = 0
n = len(coordinates)

for i in range(n-1):
    for j in range(i+1, n):
        c1 = coordinates[i]
        c2 = coordinates[j]
        
        w = abs(c1[0] - c2[0]) + 1
        h = abs(c1[1] - c2[1]) + 1

        area = max(area, w * h)

print(area)
