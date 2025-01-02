import re

data = []
with open("data/3.txt", "r") as file:
    for line in file:
        data.append(line.strip())


total = 0
enabled = True
for i in re.finditer(r"(don\'t\(\)|do\(\)|mul\(([0-9]+,[0-9]+)\))", data[0]):
    print(i.group(0), i.group(1), i.group(2), i.start(), i.end())
    if i.group(1) == "don't()":
        enabled = False
    elif i.group(1) == "do()":
        enabled = True
    elif i.group(1)[0:3] == "mul":
        if enabled:
            total += int(i.group(2).split(",")[0]) * int(i.group(2).split(",")[1])

print(total)
