res = 0

with open("input", "r") as f:
    ranges = f.read().strip().split(',')
    
    for r in ranges:
        start, end = r.split('-')

        for i in range(int(start), int(end)+1):
            s = str(i)
            mid = len(s) // 2

            if any(s == s[:l] * (len(s) // l) for l in range(1, mid+1)):
                res = res + i

print(res)
