import re
import math
file = 'data/8.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    directions = []
    paths = {}
    orig = ""
    for index, row in enumerate(data.split("\n")):
        if index == 0:
            directions = row
            continue
        if index == 1:
            continue
        m = re.match(r'(?P<source>\w+) = \((?P<l_dest>\w+), (?P<r_dest>\w+)\)', row)
        paths[m.group("source")] = {"L": m.group("l_dest"), "R": m.group("r_dest")}

        if index == 2:
            orig = m.group("source")

    print(directions)


    dest = [k for k in paths.keys() if k[2] == "A"]
    iterations = []
    for j in dest:
        print(j)
        it = 0
        mydest = j
        while mydest[2] != "Z":
            mydest = paths[mydest][directions[it % len(directions)]]
            it += 1
        iterations.append(it)
        print(j, it)
    print(iterations)
    print(math.lcm(*iterations))

    # while any([j[2] != "Z" for j in dest]):
    #     # print(dest)
    #     for index, i in enumerate(dest):
    #         dest[index] = paths[i][directions[iterations % len(directions)]]
    #     # print(dest[index], directions[iterations % len(directions)])
    #     # dest = paths[i][directions[iterations % len(directions)]]
    #     iterations += 1
    # print(iterations)