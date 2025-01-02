from collections import defaultdict

sets = defaultdict(list)

with open("data/23.txt", "r") as file:
    wd = file.read()
for line in wd.split("\n"):
    row = line.strip().split("-")
    if row[0] < row[1]:
        sets[row[0]].append(row[1])
    else:
        sets[row[1]].append(row[0])

# print(sets)

def get_biggest_group(path, intersect):
    # Given a path and their current intersect, find the biggest path
    if not intersect:
        return path
    group_values = []
    for value in sorted(intersect):
        if not value in sets.keys():
            group_values.append(path.copy() + [value])
            continue
        value_related = set(sorted(sets[value].copy()))
        yolo = get_biggest_group(path.copy() + [value], intersect.copy() & value_related.copy())
        group_values.append([i for i in yolo])
        # print("investigating", value, value_related, intersect & value_related, path, intersect)

    if max(len(i) for i in group_values) > 13:
        print(",".join(group_values[0]))
    biggest_group = [i for i in group_values if len(i) == max(len(i) for i in group_values)][0]
    return biggest_group


total = 0
max_group = set()
for key in sorted(sets.keys()):
    values = sets[key].copy()
    # print("\n", "starting", key, values)
    set(values)
    get_biggest_group([key], set(values))
