file = 'data/21.txt'

class Dot:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __repr__(self):
        return "%s-%s" % (self.row, self.col)
if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    dots = []
    moves = []
    for irow, row in enumerate(data.split("\n")):
        for icol, point in enumerate(row):
            if point in [".", "S"]:
                newdot = Dot(irow, icol)
                dots.append(newdot)
                if point == "S":
                    moves = [newdot]

    counter = 0

    while counter < 64:
        tmp_moves = []
        for i in dots:
            found = False
            for dot in moves:
                if found:
                    break
                if abs(i.row-dot.row) + abs(i.col-dot.col) == 1:
                    tmp_moves.append(i)
                    found = True
        moves = tmp_moves
        counter += 1
        print(counter)

    print(moves)
    print(len(moves))
