file = 'data/10_2_ex_2.txt'
SPECIAL_CHAR = "F"
START_INSIDE = ["n", "o"]

# file = 'data/10_2_ex_3.txt'
# SPECIAL_CHAR = "7"
# START_INSIDE = ["s", "o"]



class Pipe:

    def __init__(self, position, char):
        self.char = char
        self.special_char = char
        if self.char == "S":
            self.special_char = "S"
            self.char = SPECIAL_CHAR
        # Position is a tuple (column, row)
        self.position = position
        self.left, self.right = self.compute()
        self.in_loop = False
        self.inside = []

    def __str__(self):
        return "pipe: %s - %s" % (self.char, self.position)

    def compute(self):
        if self.char == ".":
            return None, None
        if self.char == "-":
            return (self.position[0] - 1, self.position[1]), \
            (self.position[0] + 1, self.position[1])
        if self.char == "|":
            return (self.position[0], self.position[1]-1), \
            (self.position[0], self.position[1]+1)
        if self.char == "7":
            return (self.position[0] - 1, self.position[1]), \
            (self.position[0], self.position[1]+1)
        if self.char == "J":
            return (self.position[0], self.position[1]-1), \
            (self.position[0]-1, self.position[1])
        if self.char == "L":
            return (self.position[0], self.position[1]-1), \
            (self.position[0]+1, self.position[1])
        if self.char == "F":
            return (self.position[0] + 1, self.position[1]), \
            (self.position[0], self.position[1]+1)
        raise ValueError("invalid character %s" % self.char)

    def next(self, previous):
        if self.special_char == "S":
            return self.right
        if self.left == previous:
            return self.right
        if self.right == previous:
            return self.left
        raise ValueError("not in the path:", previous)

    def set_inside(self, previous_inside, direction_from):
        print(self.char, previous_inside)
        if self.special_char == "S":
            return
        if self.char == "-":
            pos = "s" if "s" in previous_inside else "n"
            self.inside = [pos]
        if self.char == "|":
            pos = "e" if "e" in previous_inside else "o"
            self.inside = [pos]
        if self.char == "F":
            if previous_inside == ["e"] or previous_inside == ["s"]:
                self.inside = ["s", "e"]
            elif previous_inside == ["n"] or previous_inside == ["o"]:
                self.inside = ["n", "o"]

            elif direction_from == "r":
                if "s" in previous_inside:
                    self.inside = ["s", "e"]
                else:
                    self.inside = ["n", "o"]
            elif direction_from == "d":
                if "e" in previous_inside:
                    self.inside = ["s", "e"]
                else:
                    self.inside = ["n", "o"]
            else:
                raise ValueError("yolo F", direction_from)

        if self.char == "J":
            if previous_inside == ["s"] or previous_inside == ["e"]:
                self.inside = ["s", "e"]
            elif previous_inside == ["n"] or previous_inside == ["o"]:
                self.inside = ["n", "o"]

            elif direction_from == "l":
                if "s" in previous_inside:
                    self.inside = ["s", "e"]
                else:
                    self.inside = ["n", "o"]
            elif direction_from == "u":
                if "e" in previous_inside:
                    self.inside = ["s", "e"]
                else:
                    self.inside = ["n", "o"]
            else:
                raise ValueError("yolo J")

        if self.char == "7":
            if previous_inside == ["o"] or previous_inside == ["s"]:
                self.inside = ["s", "o"]
            elif previous_inside == ["n"] or previous_inside == ["e"]:
                self.inside = ["n", "e"]

            elif direction_from == "l":
                if "s" in previous_inside:
                    self.inside = ["s", "o"]
                else:
                    self.inside = ["n", "e"]
            elif direction_from == "d":
                if "o" in previous_inside:
                    self.inside = ["s", "o"]
                else:
                    self.inside = ["n", "e"]
            else:
                raise ValueError("yolo 7")

        if self.char == "L":
            if previous_inside == ["o"] or previous_inside == ["s"]:
                self.inside = ["s", "o"]
            elif previous_inside == ["n"] or previous_inside == ["e"]:
                self.inside = ["n", "e"]

            elif direction_from == "r":
                if "s" in previous_inside:
                    self.inside = ["s", "o"]
                else:
                    self.inside = ["n", "e"]
            elif direction_from == "u":
                if "o" in previous_inside:
                    self.inside = ["s", "o"]
                else:
                    self.inside = ["n", "e"]
            else:
                raise ValueError("yolo L")


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    points = []
    for irow, row in enumerate(data.split("\n")):
        for icol, char in enumerate(row):
            point = Pipe((icol, irow), char)
            points.append(point)
            if char == "S":
                start = point

    next_position = start.next("")
    start.in_loop = True
    start.inside = START_INSIDE
    prev_position = start.position
    next_point = [p for p in points if p.position == next_position][0]
    next_point.in_loop = True
    direction_from = ""
    if next_point.position[0] < prev_position[0]:
        direction_from = "r"
    if next_point.position[0] > prev_position[0]:
        direction_from = "l"
    if next_point.position[1] < prev_position[1]:
        direction_from = "d"
    if next_point.position[1] > prev_position[1]:
        direction_from = "u"
    next_point.set_inside(start.inside, direction_from)
    inside = next_point.inside
    iterations = 1
    in_loop = [start, next_point]
    while next_point != start:
        old_position = next_point.position
        next_position = next_point.next(prev_position)
        # print("iterations", iterations, next_point, next_position)
        next_point = [p for p in points if p.position == next_position][0]

        direction_from = ""
        if next_point.position[0] < old_position[0]:
            direction_from = "r"
        if next_point.position[0] > old_position[0]:
            direction_from = "l"
        if next_point.position[1] < old_position[1]:
            direction_from = "d"
        if next_point.position[1] > old_position[1]:
            direction_from = "u"
        print(direction_from)
        next_point.set_inside(inside, direction_from)
        next_point.in_loop = True
        iterations += 1
        prev_position = old_position
        in_loop.append(next_point)
        inside = next_point.inside
    print(iterations/2)

    printed_char = ""
    directions = ""
    total = 0
    for i in range(irow+1):
        for j in range(icol+1):
            point = [p for p in points if p.position == (j, i)][0]
            char = " "
            direction = "         "
            highers = [i for i in in_loop if i.position[0] == point.position[0] and i.position[1] < point.position[1]]
            lowers = [i for i in in_loop if i.position[0] == point.position[0] and i.position[1] > point.position[1]]
            righters = [i for i in in_loop if i.position[0] > point.position[0] and i.position[1] == point.position[1]]
            lefters = [i for i in in_loop if i.position[0] < point.position[0] and i.position[1] == point.position[1]]

            closest_higher = sorted(highers, key = lambda x: -x.position[1])[0] if highers else None
            closest_lower = sorted(lowers, key = lambda x: x.position[1])[0] if lowers else None
            closest_righter = sorted(righters, key = lambda x: x.position[0])[0] if righters else None
            closest_lefter = sorted(lefters, key = lambda x: -x.position[0])[0] if lefters else None
            # if closest_lefter and closest_righter and closest_lower and closest_higher:
            #     print(j, i, [str(k) for k in highers], closest_higher.position, closest_higher.inside, closest_lower.inside, closest_lefter.inside, closest_righter.inside)
            if point.in_loop:
                char = point.char
                if len(point.inside) == 2:
                    direction = " ( %s,%s ) " % (point.inside[0], point.inside[1])
                else:
                    direction = " (  %s  ) " % (point.inside[0])
                # Count number of inside in each direction
                # elif len([i for i in in_loop if i.position[0] == point.position[0] and i.position[1] < point.position[1] and "s" in i.inside]) %2 == 1:
                #     print(point)
                #     print("YOLO")
                #     char = "."
                # elif len([i for i in in_loop if i.position[0] == point.position[0] and i.position[1] > point.position[1] and "n" in i.inside]) %2 == 1:
                #     print(point)
                #     print("YOLO")
                #     char = "."

                # if we can find one point higher, one point righter, one point lefter, and one point downer, print a .

            elif not closest_lefter or not closest_righter or not closest_lower or not closest_higher:
                char = " "
                direction = "         "


            elif ("s" in closest_higher.inside and "n" in closest_lower.inside and "e" in closest_lefter.inside and "o" in closest_righter.inside):
                # elif len([i for i in in_loop if i.position[0] == point.position[0] and i.position[1] < point.position[1] and "n" in i.inside]) %2 == 1 and \
                #     len([i for i in in_loop if i.position[0] == point.position[0] and i.position[1] > point.position[1] and "s" in i.inside]) %2 == 1 and \
                #     len([i for i in in_loop if i.position[0] < point.position[0] and i.position[1] == point.position[1] and "o" in i.inside]) %2 == 1 and \
                #     len([i for i in in_loop if i.position[0] > point.position[0] and i.position[1] == point.position[1] and "e" in i.inside]) %2 == 1:
                total += 1
                char = "."
            printed_char += char
            directions += direction
        printed_char += "\n"
        directions += "\n"

    print(printed_char)
    print("\nMICHEL\n")
    print(directions)
    print("\nMICHEL\n")
    print(total)


