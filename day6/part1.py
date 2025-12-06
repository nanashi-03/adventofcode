lines = []

with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

operators = lines[-1].split()

answers = []

for operator in operators:
    answers.append(int(operator == '*'))

for line in lines[:-1]:
    nums = map(int, line.split())

    for i, num in enumerate(nums):
        if operators[i]=='*':
            answers[i] = answers[i] * num
        else:
            answers[i] = answers[i] + num

total = 0

for answer in answers:
    total = total + answer

print(total)
