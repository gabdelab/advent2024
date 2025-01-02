from collections import defaultdict
from typing import Any

def group_nodes(nodes):
    groups = {i.group: {i} for i in nodes}
    temp_groups = None
    iteration = 0
    while temp_groups != groups:
        print("grouping", iteration, len(groups))
        iteration += 1
        temp_groups = groups.copy()
        found = False
        for group_id, group_set in groups.items():
            if found:
                continue
            for group_id_2, group_set_2 in groups.items():
                if found:
                    continue
                if group_id == group_id_2:
                    continue
                if any(abs(a.row - b.row) + abs(a.col - b.col) == 1 for a in group_set for b in group_set_2):
                    groups[group_id] = group_set | group_set_2
                    groups[group_id_2] = {}
                    found = True
    for i in groups:
        if i == []:
            groups.pop(i)
    return groups

def compute_perimeter(group):
    # Check how many neighbors each point has. count 4 - nb neighbors.  
    total = 0
    for i in group:
        neighbors = 0
        for j in group:
            if abs(i.row - j.row) + abs(i.col - j.col) == 1:
                neighbors += 1
        total += 4 - neighbors
    return total

class Node:
    def __init__(self, row, col, value, group):
        self.row = row
        self.col = col
        self.value = value
        self.group = group
    def __repr__(self):
        return f"Node({self.row}, {self.col}, {self.value}, {self.group})"

data = defaultdict(list)
with open("data/12.txt", "r") as file:
    for lineno, line in enumerate(file):
        for colno, char in enumerate(line.strip().split()[0]):
            data[char].append(Node(lineno, colno, char, colno+lineno*140))

total = 0
for j in data:
    groups = group_nodes(data[j])
    print("grouped", j)
    subtotal = 0
    for group in groups.values():
        # print(j, len(group), compute_perimeter(group))
        subtotal += len(group) * compute_perimeter(group)
    total += subtotal

print(total)