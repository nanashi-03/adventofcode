joltage = 0

def get_max(arr, start, end):
    current, index = arr[start], start
    
    for i in range(start + 1, end):
        if arr[i] > current:
            current = arr[i]
            index = i

    return index

with open("input", "r") as f:
    for line in f:
        arr = []
        for n in line.strip():
            arr.append(int(n))

        joltages = [-1]
        for i in range(12):
            start = joltages[-1] + 1
            remaining_turns = 11 - i
            end = len(arr) - remaining_turns
            joltages.append(get_max(arr, start, end))

        jolt = 0
        for i in range(1, len(joltages)):
            jolt = jolt * 10
            jolt = jolt + arr[joltages[i]]
        
        joltage = joltage + jolt

print(joltage)
