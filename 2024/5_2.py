import time

def fix_item(item):
    for condition in print_conditions:
        if condition[0] in item and condition[1] in item \
            and item.index(condition[0]) > item.index(condition[1]):
            # move the second item right before the first item 
            second_idx = item.index(condition[1])
            first_idx = item.index(condition[0])
            item.insert(first_idx, item.pop(second_idx))
            return fix_item(item)
    return item

with open("data/5.txt", "r") as file:
    data = file.read().split("\n\n")

print_conditions = []
for i in data[0].split("\n"):
    print_conditions.append([int(x) for x in i.split("|")])
printed = []
for i in data[1].split("\n"):
    printed.append([int(x) for x in i.split(",")])

time_start = time.time()
to_sum = []
for printed_item in printed:
    for condition in print_conditions:
        if condition[0] in printed_item and condition[1] in printed_item \
            and printed_item.index(condition[0]) > printed_item.index(condition[1]):
            corrected_item = fix_item(printed_item)
            to_sum.append(corrected_item[int(len(corrected_item)/2)])
print(time.time() - time_start)
# print(to_sum)
print(sum(to_sum))