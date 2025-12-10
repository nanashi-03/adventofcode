from collections import deque

lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

def solve(diagram, button):
    target = tuple(diagram)
    n = len(diagram)
    current = tuple(False for i in range(n))

    visited = {current: 0}
    queue = deque([current])

    while queue:
        current = queue.popleft()
        count = visited[current] + 1

        for btn in button:
            temp = []
            for i in range(n):
                if i in btn:
                    temp.append(not current[i])
                else:
                    temp.append(current[i])
            next = tuple(temp)
            del(temp)

            if next not in visited:
                if next == target:
                    return count
                visited[next] = count
                queue.append(next)
    return None

diagrams = []
buttons = []
joltages = []

for line in lines:
    ds, *bs, js = line.split(" ")
    dia = list(i == "#" for i in ds[1:-1])
    butt = [list(map(int, b[1:-1].split(","))) for b in bs]
    jolt = list(map(int, js[1:-1].split(",")))
    diagrams.append(dia)
    buttons.append(butt)
    joltages.append(jolt)

c = sum(solve(diagram, button) for diagram, button in zip(diagrams, buttons))
print(c)
