file = 'data/3.txt'


class Point:

    def __init__(self, row, start, end, value):
        self.row = row
        self.end = end
        self.start = start
        self.value = value
        self.is_countable = False

    def __str__(self):
        return "row %d - value %s - index %s to %s" % (self.row, self.value, self.start, self.end)

    def isvalue(self):
        return str(self.value).isdigit()

    def set_is_countable(self):
        self.is_countable = True


def is_adjacent(point1, point2):
    if point1 == point2:
        return False
    if abs(point1.row - point2.row) < 2 and \
        (abs(point1.start-point2.end) < 2 or abs(point2.start-point1.end) <2):
        return True
    return False


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    points = []
    for irow, row in enumerate(data.split("\n")):
        previous_bit = "."
        current_int = ""
        start = 0
        for index, char in enumerate(row):
            if previous_bit.isdigit() and not char.isdigit():
                points.append(Point(irow, start, index-1, int(current_int)))
                previous_bit = "."
                current_int = ""
                start = None
                if char != ".":
                    points.append(Point(irow, index, index, char))
                continue
            if char == ".":
                previous_bit = char
                continue
            if not char.isdigit():
                previous_bit = char
                points.append(Point(irow, index, index, char))
                continue
            if previous_bit.isdigit():
                current_int += char
                if previous_bit is None:
                    previous_bit = char
                    start = index
            if not previous_bit.isdigit():
                start = index
                previous_bit = char
                current_int = char
            if index == len(row)-1 and current_int:
                points.append(Point(irow, start, index, int(current_int)))
    print("\n".join([str(i) for i in points]))
    total = 0
    for i in points:
        if not i.isvalue():
            continue
        if any([is_adjacent(i, j) for j in points if not j.isvalue()]):
            print(i.value)
            total += i.value
    print(total)
