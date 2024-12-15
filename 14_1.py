import re

nb_iter = 100
size_top = 103
size_left = 101


data = []
pattern = r"p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)"
with open("data/14.txt", "r") as file:
    wd = file.read()
    for line in wd.split("\n"):
        match = re.search(pattern, line)
        if match:
            data.append([int(x) for x in match.groups()])

quarter_topleft = 0
quarter_topright = 0
quarter_bottomleft = 0
quarter_bottomright = 0
for row in data:
    dest_row = (row[0] + row[2] * nb_iter) % size_left
    dest_col = (row[1] + row[3] * nb_iter) % size_top
    if dest_row < size_left // 2 and dest_col < size_top // 2:
        quarter_topleft += 1
    elif dest_row < size_left // 2 and dest_col > size_top // 2:
        quarter_topright += 1
    elif dest_row > size_left // 2 and dest_col < size_top // 2:
        quarter_bottomleft += 1
    elif dest_row > size_left // 2 and dest_col > size_top // 2:
        quarter_bottomright += 1
print(quarter_topleft, quarter_topright, quarter_bottomleft, quarter_bottomright)
print(quarter_topleft * quarter_topright * quarter_bottomleft * quarter_bottomright)
