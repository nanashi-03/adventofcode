lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

routes = {}

for line in lines:
    src, dest = line.split(": ")
    dest = dest.split()
    routes[src] = dest

cache = {}

def dfs(current, end):
    if current == end:
        return 1
    if current in cache:
        return cache[current]
    
    count = 0
    for next in routes.get(current, []):
        count = count + dfs(next, end)
    cache[current] = count
    return count

print(dfs('you', 'out'))
