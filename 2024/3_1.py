import re

data = []
with open("data/3.txt", "r") as file:
    for line in file:
        data.append(line.strip())

total = 0

for i in re.findall(r"mul\(([0-9]+,[0-9]+)\)", data[0]):
    l = i.split(",")
    total += int(l[0]) * int(l[1])

print(total)