pos = 50
count = 0

with open("input", "r") as f:
    for line in f:
        print(line)
        steps = int(line[1:])
        if line[0] == 'L':
            try:
                count = count + abs(pos - steps) // 100 + (pos != 0 and pos <= steps)  
                pos = (pos - steps) % 100
            except Exception as e:
                raise e

        else:
            try:
                count = count + (pos + steps) // 100 
                pos = (pos + steps) % 100
            except Exception as e:
                raise e

print(count)
