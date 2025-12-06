lines = []

with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line)

rows, columns = len(lines), len(lines[0]) - 1

total = 0
nums = []

for c in range(columns - 1, -1, -1):
    curr = 0

    for r in range(rows):
        n = lines[r][c]

        if n.isnumeric():
            curr = curr * 10
            curr = curr + int(n)

        if r == rows - 1 and curr != 0:
            nums.append(curr)
            curr = 0

        if n in "+*":
            acc = 1 if n == "*" else 0

            for num in nums:
                if n == "*":
                    acc = acc * num
                else:
                    acc = acc + num
                
            total += acc
            nums = []

print(total)
