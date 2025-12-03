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

        max1 = get_max(arr, 0, len(arr) - 1)
        max2 = get_max(arr, max1 + 1, len(arr))
        
        joltage = joltage + 10*arr[max1] + arr[max2]

print(joltage)
