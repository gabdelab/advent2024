from collections import defaultdict

sets = defaultdict(list)

with open("data/23.txt", "r") as file:
    wd = file.read()
for line in wd.split("\n"):
    row = line.strip().split("-")
    sets[row[0]].append(row[1])
    sets[row[1]].append(row[0])

total = 0
outcomes = set()
for key, values in sets.items():
    for value in values:
        intersect = set(values).intersection(set(sets[value]))
        for triangle in intersect:
            if key[0] == "t" or triangle[0] == "t" or value[0] == "t":
                outcomes.add("-".join(sorted([key, value, triangle])))
print(len(outcomes))
