def fix_item(item):
    for condition in print_conditions:
        if condition[0] in item and condition[1] in item \
            and item.index(condition[0]) > item.index(condition[1]):
            item[item.index(condition[0])], item[item.index(condition[1])] = \
                item[item.index(condition[1])], item[item.index(condition[0])]
            return fix_item(item)
    return item

data = []
with open("data/5.txt", "r") as file:
    data = file.read().split("\n\n")
    conditions = data[0]
    printings = data[1]

print_conditions = []
for i in conditions.split("\n"):
    print_conditions.append([int(x) for x in i.split("|")])
printed = []
for i in printings.split("\n"):
    printed.append([int(x) for x in i.split(",")])

to_sum = []
for printed_item in printed:
    correct = True
    for condition in print_conditions:
        if condition[0] in printed_item and condition[1] in printed_item \
            and printed_item.index(condition[0]) > printed_item.index(condition[1]):
            correct = False
            corrected_item = fix_item(printed_item)
            print(corrected_item)
            to_sum.append(corrected_item[int(len(corrected_item)/2)])
    if correct:
        continue

print(to_sum)
print(sum(to_sum))