file = 'data/10.txt'
SPECIAL_CHAR = "F"

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

    def __str__(self):
        return "pipe: %s - %s" % (self.char, self.position)

    def compute(self):
        if self.char == ".":
            print("should not be here", self.position)
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
        print("char: %s - position %s - prev %s - nextL %s - nextR %s"% (self.special_char, self.position, previous, self.right, self.left))
        if self.special_char == "S":
            return self.right
        if self.left == previous:
            return self.right
        if self.right == previous:
            return self.left
        raise ValueError("not in the path:", previous)

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
    prev_position = start.position
    next_point = [p for p in points if p.position == next_position][0]
    iterations = 1
    while next_point != start:
        old_position = next_point.position
        next_position = next_point.next(prev_position)
        print("iterations", iterations, next_point, next_position)
        next_point = [p for p in points if p.position == next_position][0]
        iterations += 1
        prev_position = old_position

    print(iterations/2)
