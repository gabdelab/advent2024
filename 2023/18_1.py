file = 'data/1.txt'

def from_direction(row, col, direction):
    if direction == "R":
        return row, col+1
    if direction == "U":
        return row-1, col
    if direction == "D":
        return row+1, col
    if direction == "L":
        return row, col-1

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    points = {i: [] for i in range(500)}
    row, col = 250, 250
    for datarow in data.split("\n"):
        direction, length, color = datarow.split(" ")
        for i in range(int(length)):
            row, col = from_direction(row, col, direction)
            points[row].append(col)

    total = 0
    print(points)
    for i in range(500):
        if not points[i]:
            continue
        row_points = sorted(points[i])
        print("before", i, row_points)
        row_total = 0
        outside = True
        while row_points:
            first_point = row_points[0]
            if len(row_points) == 1:
                print("if", row_points, outside)
                row_total += 1
                row_points = []
                outside = not outside
            else:
                next_sequence = [row_points[0]]
                index = 1
                while index < len(row_points) and row_points[index] == next_sequence[-1] + 1:
                    next_sequence.append(row_points[index])
                    index += 1
                start_downer = len([p for p in points[i+1] if p == next_sequence[0]]) > 0
                start_upper = len([p for p in points[i-1] if p == next_sequence[0]]) > 0
                end_upper = len([p for p in points[i-1] if p == next_sequence[-1]]) > 0
                end_downer = len([p for p in points[i+1] if p == next_sequence[-1]]) > 0
                if next_sequence == row_points:
                    print("outside is outside")
                    outside = outside
                elif (start_upper and end_downer) or (start_downer and end_upper):
                    print("flipping the coin")
                    outside = not outside
                else:
                    print("none of them", start_downer, start_upper, end_upper, end_downer)

                if row_points[1] == row_points[0] + 1:
                    # Case where we enter a streak of consecutive points
                    print("elif", row_points, outside)
                    while len(next_sequence) > 1:
                        row_total += 1
                        next_sequence.pop(0)
                        row_points.pop(0)
                else:
                    print("else", row_points, outside, next_sequence)
                    # Case where we have one point then the other one is further
                    if outside:
                        row_total += 1
                    else:
                        row_total += row_points[1] - row_points[0]
                    row_points.pop(0)

        total += row_total
        print("after", i, row_total)
    print(total)

