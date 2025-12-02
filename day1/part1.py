pos = 50
count = 0

with open("input", "r") as f:
    for line in f:
        print(line)
        if line[0] == 'L':
            try:
                pos = pos - int(line[1:])
            except Exception as e:
                raise e

        else:
            try:
                pos = pos + int(line[1:])
            except Exception as e:
                raise e

        pos = pos % 100
        
        if pos == 0:
            count = count + 1


        count = count + 1

print(count)
