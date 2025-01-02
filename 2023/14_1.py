file = 'data/14_ex.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    squareR = []
    roundR = []
    for irow, row in enumerate(data.split("\n")):
        for icol, char in enumerate(row):
            if char == "#":
                squareR.append((irow, icol))
            if char == "O":
                roundR.append((irow, icol))
    nb_row = irow + 1

    total = 0
    for rock in roundR:
        closest_north = [r for r in squareR if r[1] == rock[1] and r[0] < rock[0]]
        if not closest_north:
            total += nb_row
            squareR.append((0, rock[1]))
            continue
        closest_north = sorted(closest_north, key = lambda r: -r[0])[0]

        total += nb_row - closest_north[0] - 1
        squareR.append((closest_north[0]+1, rock[1]))
    print(len(squareR))
    print(sorted(squareR))
    print(total)


4 -> 11 -> 18 -> 