from collections import defaultdict


def group_nodes(nodes):
    groups = {i.group: {(i.row, i.col)} for i in nodes}
    temp_groups = None
    iteration = 0
    while temp_groups != groups:
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
                if any(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a in group_set for b in group_set_2):
                    groups[group_id] = group_set | group_set_2
                    groups[group_id_2] = {}
                    found = True
    for i in groups:
        if i == []:
            groups.pop(i)
    return groups

def find_corners_arrow(point1, point2, point3):
    # Given 3 points, find if the arrow they form is pointing up, down, left or right
    # and return the 2 points that would create a C shape from them
    min_x = min(point1[0], point2[0], point3[0])
    max_x = max(point1[0], point2[0], point3[0])
    min_y = min(point1[1], point2[1], point3[1])
    max_y = max(point1[1], point2[1], point3[1])
    if max_y - min_y == 2:
        # it points up or down
        if int(point1[0] == min_x) + int(point2[0] == min_x) + int(point3[0] == min_x) == 2:
            # it points down 
            return (max_x, min_y), (max_x, max_y)
        # it points up
        return (min_x, min_y), (min_x, max_y)
    # it points left or right
    if int(point1[1] == min_y) + int(point2[1] == min_y) + int(point3[1] == min_y) == 2:
        # it points right
        return (min_x, max_y), (max_x, max_y)
    # it points left
    return (min_x, min_y), (max_x, min_y)

def find_opposite_corner(point1, point2, point3):
    # given 3 points shaped as a x in the pictures below
    # - . .        . . -       . x .
    # . x x        x x .       x x .
    # . x .        . x .       . . -
    # return the point shaped as a dash
    # note : point3 is always at the center of the V shape

    if point3[0] == min(point1[0], point2[0]):
        row = point3[0] - 1
    else: 
        row = point3[0] + 1
    if point3[1] == min(point1[1], point2[1]):
        col = point3[1] - 1
    else:
        col = point3[1] + 1
    return (row, col)


def compute_nb_sides(group):
    # Check how many sides each group has.

    # compter le nombre de sides revient à compter le nombre de coins
    # Un coin est défini par: 
    # - coin convexe: 
    #     - Soit 2 voisins qui ne sont pas alignés , 
    #     - Soit 1 seul voisin, qui ramènera 2 coins dans ce cas là
    # - coin concave: (0, 0), (0, 1) et (1, 0) sont là mais pas (1, 1)
    #     - Soit 2 voisins et le point qui est en (1, 1) n'est pas là
    #     - Soit 3 voisins et on vérifie les 2 points qui sont du côté des 3 voisins
    #     - Soit 4 voisins et on les vérifie tous

    concave_total = 0
    convex_total = 0
    for i in group:
        concave = 0
        convex = 0
        neighbors = []
        for j in group:
            if abs(i[0] - j[0]) + abs(i[1] - j[1]) == 1:
                neighbors.append(j)
        
        if len(neighbors) == 0:
            convex += 4

        if len(neighbors) == 1:
            convex += 2

        if len(neighbors) == 2:
            # If the 2 neighbors are on the same line or column, it's a line, it means no turn
            if neighbors[0][0] == neighbors[1][0] or neighbors[0][1] == neighbors[1][1]:
                continue
            # Convex should always be +1 except if we have this shape:
            # x . .
            # . x x
            # . x x
            # in this case, it's not a convex, it's 2 different shapes so we shouldn't count the convex
            convex += 1
            (row, col) =  find_opposite_corner(neighbors[0], neighbors[1], i)
            if (row, col) in group:
                convex -= 1
                concave += 1
        
            if neighbors[0][0] == i[0]:
                if (neighbors[1][0], neighbors[0][1]) not in group:
                    concave += 1
            else:
                if (neighbors[0][0], neighbors[1][1]) not in group:
                    concave += 1

        if len(neighbors) == 3:
            # Find the orientation of the podium and look for the 2 missing bits
            corner1, corner2 = find_corners_arrow(neighbors[0], neighbors[1], neighbors[2])
            found1 = False
            found2 = False
            if corner1 not in group:
                concave += 1
                found1 = True
            if corner2 not in group:
                concave += 1
                found2 = True

        if len(neighbors) == 4:
            # check all 4 corners
            if (i[0]-1, i[1]-1) not in group:
                concave += 1
            if (i[0]-1, i[1]+1) not in group:
                concave += 1
            if (i[0]+1, i[1]-1) not in group:
                concave += 1
            if (i[0]+1, i[1]+1) not in group:
                concave += 1
        concave_total += concave
        convex_total += convex

    return concave_total, convex_total

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
    subtotal = 0
    for group in groups.values():
        if len(group) == 0:
            continue
        concave, convex = compute_nb_sides(group)
        print("computing sides", j, len(group), concave, convex)
        subtotal += len(group) * (concave + convex)
    total += subtotal

print(total)