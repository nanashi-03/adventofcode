with open("input", "r") as f:
    lines = f.readlines()

coordinates = []
for line in lines:
    coordinates.append(list(map(int, line.split(','))))

n = len(coordinates)

def intersect(p1, p2, q1, q2):
    px_min = min(p1[0], p2[0])
    px_max = max(p1[0], p2[0])
    py_min = min(p1[1], p2[1])
    py_max = max(p1[1], p2[1])
    qx_min = min(q1[0], q2[0])
    qx_max = max(q1[0], q2[0])
    qy_min = min(q1[1], q2[1])
    qy_max = max(q1[1], q2[1])

    intersection = qx_max > px_min and qx_min < px_max and qy_max > py_min and qy_min < py_max
    return intersection

def is_valid(p1, p2):
    q1 = coordinates[-1]
    for q2 in coordinates:
        if intersect(p1, p2, q1, q2):
            return False
        q1 = q2
    return True

area = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        c1, c2 = coordinates[i], coordinates[j]
        
        w = abs(c1[0] - c2[0]) + 1
        h = abs(c1[1] - c2[1]) + 1
        a = w * h
        
        if a > area and is_valid(c1, c2):
            area = a

print(area)
