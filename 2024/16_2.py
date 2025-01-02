from collections import defaultdict

#BEST_COST = 7036 # Ex 1
# BEST_COST = 11048 # Ex 2
BEST_COST = 143580 # real data
FILENAME = "data/16.txt"


def next_position(current_position, current_direction):
    global out
    if current_direction == "N":
        return out[current_position.row - 1][current_position.col]
    elif current_direction == "E":
        return out[current_position.row][current_position.col + 1]
    elif current_direction == "S":
        return out[current_position.row + 1][current_position.col]
    elif current_direction == "W":
        return out[current_position.row][current_position.col - 1]

def find_best_path(out, current_position, current_direction, current_cost, current_path, just_turned = False):
    if min_costs[current_position.row][current_position.col][current_direction] < current_cost:
        return float("inf")
    min_costs[current_position.row][current_position.col][current_direction] = current_cost
    if out[current_position.row][current_position.col].value == "#":
        return float("inf")
    global min_cost, directions, sitting_spots
    if current_cost > min_cost:
        return float("inf")
    if out[current_position.row][current_position.col].value == "E":
        if current_cost == BEST_COST:
            print(current_path)
            sitting_spots.update(set(current_path))
        if current_cost < min_cost:
            min_cost = current_cost
            print(min_cost)
        return current_cost
    if current_position in set(current_path[:-1]):
        return float("inf")
    current_path.append(current_position)
    best_path_forward = find_best_path(out, next_position(current_position, current_direction), current_direction, current_cost+1, current_path.copy(), False)
    if not just_turned:
        best_path_clockwise = find_best_path(out, current_position, directions[(directions.index(current_direction) + 1) % 4], current_cost+1000, current_path.copy(), True)
        best_path_counterclockwise = find_best_path(out, current_position, directions[(directions.index(current_direction) - 1) % 4], current_cost+1000, current_path.copy(), True)
    else:
        best_path_clockwise = float("inf")
        best_path_counterclockwise = float("inf")

    return min(best_path_forward, best_path_clockwise, best_path_counterclockwise)


class Point():
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.is_current = False
        if self.value == "S":
            self.is_current = True
            self.value = "."

    def __repr__(self):
        return f"({self.row}, {self.col})"

out = defaultdict(lambda: defaultdict(lambda: None))
with open(FILENAME, "r") as file:
    for irow, line in enumerate(file):
        for icol, col in enumerate(line.strip()):
            out[irow][icol] = Point(irow, icol, col)

current_position = [i for k in out.values() for i in k.values() if i.is_current][0]


sitting_spots = set()

directions = ["N", "E", "S", "W"]
current_direction = "E"
min_cost = float(210000)
min_costs = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: float("inf"))))
find_best_path(out, current_position, current_direction, 0, [], False)


print(len(sitting_spots)+1)