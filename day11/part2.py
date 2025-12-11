lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

routes = {}

for line in lines:
    src, dest = line.split(": ")
    dest = dest.split()
    routes[src] = dest

def count_paths(start, end):
    if start not in routes:
        return 0

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

    return dfs(start, end)

count_sd = count_paths('svr', 'dac')
count_df = count_paths('dac', 'fft')
count_fo = count_paths('fft', 'out')

count_sf = count_paths('svr', 'fft')
count_fd = count_paths('fft', 'dac')
count_do = count_paths('dac', 'out')

count_sdfo = count_sd * count_df * count_fo
count_sfdo = count_sf * count_fd * count_do

count = count_sdfo + count_sfdo

print(count)
