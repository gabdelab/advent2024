import re

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
        print(m)
        print(row)
        print(m.group('source'), m.group('l_dest'), m.group('r_dest'))

        paths[m.group("source")] = {"L": m.group("l_dest"), "R": m.group("r_dest")}

        if index == 2:
            orig = m.group("source")

    print(directions)

    dest = "AAA"
    iterations = 0
    while dest != "ZZZ":
        print(dest, directions[iterations % len(directions)])
        dest = paths[dest][directions[iterations % len(directions)]]
        iterations += 1
    print(iterations)