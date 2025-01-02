file = 'data/14.txt'

def yoloprinter(rocks, nb_row, nb_col):
    orig = "\n".join(["."*nb_col for _ in range(nb_row)])

    for i in rocks:
        char = "#"
        if i[2] == False:
            char = "O"
        itochange = (nb_col + 1) * i[0] + i[1] 
        orig = orig[:itochange] + char + orig[itochange+1:]
    print("current state of the rocks \n%s" % orig)



if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    rocks = []
    for irow, row in enumerate(data.split("\n")):
        for icol, char in enumerate(row):
            if char == "#":
                rocks.append((irow, icol, True))
            if char == "O":
                rocks.append((irow, icol, False))
    nb_row = irow + 1
    nb_col = icol + 1

    # yoloprinter(rocks, nb_row, nb_col)
    prev = {}
    prev[str(rocks)] = (0, 0)
    total = 0
    for i in range(1000000000):
        if i % 10000 == 0:
            print(i)
        print(len(prev))
        # Move north
        sortedrocks = sorted(rocks, key=lambda x: x[0])
        for index, rock in enumerate(sortedrocks):
            if rock[2] == True:
                continue
            closest_north = [r for r in sortedrocks if r[1] == rock[1] and r[0] < rock[0]]
            if not closest_north:
                sortedrocks[index] = (0, rock[1], False)
                continue
            closest_north = sorted(closest_north, key = lambda r: -r[0])[0]
            sortedrocks[index] = (closest_north[0]+1, rock[1], False)
        rocks = sortedrocks
        # Move west
        sortedrocks = sorted(rocks, key=lambda x: x[1])
        for index, rock in enumerate(sortedrocks):
            if rock[2] == True:
                continue
            closest_west = [r for r in sortedrocks if r[0] == rock[0] and r[1] < rock[1]]
            if not closest_west:
                sortedrocks[index] = (rock[0], 0, False)
                continue
            closest_west = sorted(closest_west, key = lambda r: -r[1])[0]
            sortedrocks[index] = (rock[0], closest_west[1]+1, False)
        rocks = sortedrocks

        # Move south
        sortedrocks = sorted(rocks, key=lambda x: -x[0])
        for index, rock in enumerate(sorted(sortedrocks, key=lambda x: -x[0])):
            if rock[2] == True:
                continue
            closest_south = [r for r in sortedrocks if r[1] == rock[1] and r[0] > rock[0]]
            if not closest_south:
                sortedrocks[index] = (nb_row-1, rock[1], False)
                continue
            closest_south = sorted(closest_south, key = lambda r: r[0])[0]
            sortedrocks[index] = (closest_south[0]-1, rock[1], False)
        rocks = sortedrocks


        # Move east
        sortedrocks = sorted(rocks, key=lambda x: -x[1])
        for index, rock in enumerate(sortedrocks):
            if rock[2] == True:
                continue
            closest_east = [r for r in sortedrocks if r[0] == rock[0] and r[1] > rock[1]]
            if not closest_east:
                sortedrocks[index] = (rock[0], nb_col - 1, False)
                continue
            closest_east = sorted(closest_east, key = lambda r: r[1])[0]
            sortedrocks[index] = (rock[0], closest_east[1]-1, False)
        rocks = sortedrocks
        # yoloprinter(rocks, nb_row, nb_col)

        if str(rocks) in prev.keys():
            found = [j[0] for i, j in prev.items() if i == str(rocks)][0]

            stop_at = (1000000000-found) %(i+1-found) + found
            print(prev.values())
            print("stopping", stop_at, found, i+1, [j[1] for j in prev.values() if j[0] == stop_at])
            break
        prev[str(rocks)] = (i + 1, sum([nb_row-i[0] for i in rocks if i[2] == False]))
    print(sum([10-i[0] for i in rocks if i[2] == False]))
