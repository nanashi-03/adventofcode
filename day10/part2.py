from z3 import Optimize, Int, sat

lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

def parse(line):
    parts = []
    for l in line.split(' '):
        parts.append(l[1:-1])

    ds, *bs, js = parts
    buttons = tuple(tuple(map(int, b.split(','))) for b in bs)
    diagrams = tuple(d == '#' for d in ds)
    jolts = tuple(map(int, js.split(',')))
    return buttons, diagrams, jolts

def solve(buttons, target):
    presses = [Int(f'p{i}') for i in range(len(buttons))]

    opt = Optimize()
    for p in presses:
        opt.add(p >= 0)

    accs = {i: 0 for i in range(len(target))}

    for p, bs in zip(presses, buttons):
        for b in bs:
            accs[b] += p

    for i in range(len(target)):
        opt.add(accs[i] == target[i])

    opt.minimize(sum(presses))

    assert opt.check() == sat

    m = opt.model()
    s = 0
    for p in presses:
        try:
            s = s + int(m[p].as_long())
        except Exception as e:
            print(e)

    return s

res = 0

for line in lines:
    buttons, diagrams, jolts = parse(line)
    sol = solve(buttons, jolts)
    res = res + sol

print(res)
