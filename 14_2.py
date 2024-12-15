import glob
import os
import re
import statistics
size_top = 103
size_left = 101
out_dir = "results"


data = []
pattern = r"p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)"
with open("data/14.txt", "r") as file:
    wd = file.read()
    for line in wd.split("\n"):
        match = re.search(pattern, line)
        if match:
            data.append([int(x) for x in match.groups()])

files = glob.glob(f"{out_dir}/14_2/*")
for f in files:
    os.remove(f)

out = []
for nb_iter in range(30000):
    print(nb_iter, data[0])
    quarter_topleft = 0
    quarter_topright = 0
    quarter_bottomleft = 0
    quarter_bottomright = 0
    centered = 0
    new_data = []
    for row in data:
        dest_row = (row[0] + row[2] ) % size_left
        dest_col = (row[1] + row[3] ) % size_top
        if dest_row < size_left // 2 and dest_col < size_top // 2:
            quarter_topleft += 1
        elif dest_row < size_left // 2 and dest_col > size_top // 2:
            quarter_topright += 1
        elif dest_row > size_left // 2 and dest_col < size_top // 2:
            quarter_bottomleft += 1
        elif dest_row > size_left // 2 and dest_col > size_top // 2:
            quarter_bottomright += 1
        if dest_row > 20 and dest_row < 80 and dest_col > 20 and dest_col < 80:
            centered += 1
        new_data.append((dest_row, dest_col, row[2], row[3]))
    data = new_data


    if centered < 200 and quarter_topleft < 200 and quarter_topright < 200 and quarter_bottomleft < 200 and quarter_bottomright < 200:
        continue
    new_data = [(x[0], x[1]) for x in data]
    out_str = ""
    for row in range(size_top):
        for col in range(size_left):
            if (row, col) in new_data:
                out_str += "#"
            else:
                out_str += "."
        out_str += "\n"

    file = open(f"{out_dir}/14_2/{nb_iter}.txt", "w")
    file.write(out_str)
    file.close()

