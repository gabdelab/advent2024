import itertools

TEST = False
FILENAME = "data/21_ex.txt" if TEST else "data/21.txt"
NB_ITERATIONS = 2 if TEST else 25

NUMERICAL_KEYBOARD = {
    0: {0: "7", 1: "8", 2: "9"},
    1: {0: "4", 1: "5", 2: "6"},
    2: {0: "1", 1: "2", 2: "3"},
    3: {1: "0", 2: "A"}
}
REVERSE_NUMERICAL_KEYBOARD = {
    "0": (3, 1),
    "A": (3, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2)
}

DIGITAL_KEYBOARD = {
    0: {1: "^", 2: "A"},
    1: {0: "<", 1: "v", 2: ">"}
}

REVERSE_DIGITAL_KEYBOARD = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

# Store the best way to go from the root key to the target key
BEST_NUMERICAL_PATHS = {
    "0": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "1": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "2": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "3": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "4": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "5": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "6": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "7": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "8": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "9": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []},
    "A": {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "A": []}
}

BEST_DIGITAL_PATHS = {
    ">": {">": [], "<": [], "^": [], "v": [], "A": []},
    "<": {">": [], "<": [], "^": [], "v": [], "A": []},
    "^": {">": [], "<": [], "^": [], "v": [], "A": []},
    "v": {">": [], "<": [], "^": [], "v": [], "A": []},
    "A": {">": [], "<": [], "^": [], "v": [], "A": []}
}

INITIAL_TRANSITIONS = {
    ">": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
    "<": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
    "^": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
    "v": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
    "A": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0}
}

def generate_empty():
    return {
        ">": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
        "<": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
        "^": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
        "v": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0},
        "A": {">": 0, "<": 0, "^": 0, "v": 0, "A": 0}
    }

def find_best_path(point_from, point_to, iter=0):
    if iter > 20:
        return []
    if point_from == point_to:
        return ["A"]
    coord_from = REVERSE_DIGITAL_KEYBOARD[point_from]
    coord_to = REVERSE_DIGITAL_KEYBOARD[point_to]

    if coord_from[0] == coord_to[0]:
        if coord_from[1] < coord_to[1]:
            return [">"] * (coord_to[1] - coord_from[1]) + ["A"]
        return ["<"] * (coord_from[1] - coord_to[1]) + ["A"]
    if coord_from[1] == coord_to[1]:
        if coord_from[0] < coord_to[0]:
            return ["v"] * (coord_to[0] - coord_from[0]) + ["A"]
        return ["^"] * (coord_from[0] - coord_to[0]) + ["A"]

    horizontal_path = []
    vertical_path = []
    if coord_from[0] < coord_to[0]:
        vertical_path = ["v"] * (coord_to[0] - coord_from[0])
    else:
        vertical_path = ["^"] * (coord_from[0] - coord_to[0])
    if coord_from[1] < coord_to[1]:
        horizontal_path = [">"] * (coord_to[1] - coord_from[1])
    else:
        horizontal_path = ["<"] * (coord_from[1] - coord_to[1])

    # The path contains both vertical and horizontal movement. 
    # Check if both are valid. If so, return the shortest one, possibly by iterations.
    try:
        # Stay on the same row, change column
        DIGITAL_KEYBOARD[coord_from[0]][coord_to[1]]
    except KeyError:
        # If this move is forbidden, the only possible path is to start by changing rows
        return vertical_path + horizontal_path + ["A"]
    
    try:
        # Stay on the same column, change row
        DIGITAL_KEYBOARD[coord_to[0]][coord_from[1]]
    except KeyError:
        # If this move is forbidden, the only possible path is to start by changing rows
        return horizontal_path + vertical_path + ["A"]
    
    # Last case: both paths are valid. Return the shortest one.
    path_a = vertical_path + horizontal_path + ["A"]
    path_b = horizontal_path + vertical_path + ["A"]

    local_a = []
    local_b = []
    for i in range(len(path_a)-1):
        local_a += find_best_path(path_a[i], path_a[i+1], iter=iter+1)
        local_b += find_best_path(path_b[i], path_b[i+1], iter=iter+1)
    if len(local_a) < len(local_b):
        return path_a   
    return path_b

def find_best_paths():
    for key, values in BEST_DIGITAL_PATHS.items():
        for value, path in values.items():
            if not path:
                BEST_DIGITAL_PATHS[key][value] = find_best_path(key, value)

def process_with_transitions(transitions):
    tmp_transitions = generate_empty()
    for point_from, value in transitions.items():
        for point_to, occurences in value.items():
            if occurences > 0:
                best_path = BEST_DIGITAL_PATHS[point_from][point_to]
                tmp_transitions["A"][best_path[0]] += transitions[point_from][point_to]
                for i in range(len(best_path)-1):
                    tmp_transitions[best_path[i]][best_path[i+1]] += transitions[point_from][point_to]
    transitions = tmp_transitions
    return transitions

def process_one_keyboard(line, is_numerical=True):
    # Given a line ex. 029A, return all possible lines to get there
    keyboard = NUMERICAL_KEYBOARD if is_numerical else DIGITAL_KEYBOARD
    reverse_keyboard = REVERSE_NUMERICAL_KEYBOARD if is_numerical else REVERSE_DIGITAL_KEYBOARD
    current_pos = reverse_keyboard["A"]
    out = []

    for char in line:
        char_pos = reverse_keyboard[char]

        if char_pos == current_pos:
            if not out:
                out = [["A"]]
            else:
                out = [i + ["A"] for i in out]
        else:
            delta = (char_pos[0] - current_pos[0], char_pos[1] - current_pos[1])
            # note: no need to do ex. left - up - left. this always lose to left-left-up or up-left-left
            # so, we can just do vertical then horizontal , or the opposite
            path_vertical = []
            path_horizontal = []
            if delta[0] > 0:
                # look down by the amount of delta
                path_vertical = ["v"] * delta[0]
            if delta[0] < 0:
                # look up by the amount of delta
                path_vertical = ["^"] * abs(delta[0])
            if delta[1] > 0:
                # look right by the amount of delta
                path_horizontal = [">"] * delta[1]
            if delta[1] < 0:
                # look left by the amount of delta
                path_horizontal = ["<"] * abs(delta[1])
            if not path_vertical:
                if not out:
                    out = [path_horizontal + ["A"]]
                else:
                    out = [i + path_horizontal + ["A"] for i in out]
            elif not path_horizontal:
                if not out:
                    out = [path_vertical + ["A"]]
                else:
                    out = [i + path_vertical + ["A"] for i in out]
            else:
                path_one = path_vertical + path_horizontal + ["A"]
                path_two = path_horizontal + path_vertical + ["A"]
                exclude_path_one, exclude_path_two = False, False
                try:
                    keyboard[current_pos[0]][char_pos[1]]
                except KeyError:
                    # Impossible to move the column
                    exclude_path_two = True
                try:
                    keyboard[char_pos[0]][current_pos[1]]
                except KeyError:
                    # Impossible to move the row
                    exclude_path_one = True
                if "".join(line) == "<<^^A>A>AvvA" and char == "<" and current_pos == (0, 2):
                    print("found yoloswag", exclude_path_one, exclude_path_two)
                if exclude_path_two:
                    if not out:
                        out = [path_one]
                    else:
                        out = [i + path_one for i in out]
                elif exclude_path_one:
                    if not out:
                        out = [path_two]
                    else:
                        out = [i + path_two for i in out]
                else:
                    # print(path_horizontal, path_horizontal, out, char, char_pos, delta)
                    if not out:
                        out = [path_one, path_two]
                    else:
                        out = [i + path_one for i in out] + [i + path_two for i in out]
        out = [i for i in out if len(i) == min(len(i) for i in out)]
        current_pos = reverse_keyboard[char]
    min_len = min(len(i) for i in out)
    return [i for i in out if len(i) == min_len]


def process(line):
    lines = process_one_keyboard(line, is_numerical=True)
    min_lines = [i for i in lines if len(i) == min(len(i) for i in lines)]
    min_len_transitions = float("inf")
    for line in min_lines:
        transitions = generate_empty()
        transitions["A"][line[0]] += 1
        for i in range(len(line) - 1):
            transitions[line[i]][line[i+1]] += 1
        for _ in range(NB_ITERATIONS):  
            transitions = process_with_transitions(transitions)
        subtotal = 0
        for _, j in transitions.items():
            for _, k in j.items():
                subtotal += k
        min_len_transitions = min(min_len_transitions, subtotal)
    return min_len_transitions

data = []
with open(FILENAME, "r") as file:
    for line in file:
        data.append(line.strip())
print(data)

find_best_paths()
print(BEST_DIGITAL_PATHS)

BEST_DIGITAL_PATHS =  {'>': {
    '>': ['A'], 
    '<': ['<', '<', 'A'], 
    '^': ['<', '^', 'A'], 
    'v': ['<', 'A'], 
    'A': ['^', 'A']}, 
  '<': {
    '>': ['>', '>', 'A'], 
    '<': ['A'], 
    '^': ['>', '^', 'A'], 
    'v': ['>', 'A'], 
    'A': ['>', '>', '^', 'A']}, 
  '^': {
    '>': ['v', '>', 'A'], 
    '<': ['v', '<','A'], 
    '^': ['A'], 
    'v': ['v', 'A'], 
    'A': ['>', 'A']}, 
  'v': {
    '>': ['>', 'A'], 
    '<': ['<', 'A'], 
    '^': ['^', 'A'], 
    'v': ['A'], 
    'A': ['^','>',  'A']}, 
  'A': {
    '>': ['v', 'A'], 
    '<': ['v', '<', '<', 'A'], 
    '^': ['<', 'A'], 
    'v': ['<', 'v', 'A'], 
    'A': ['A']}
}

total = 0
for line in data:
    min_len_transitions = process(line)
    integer = int(line[:-1])
    subtotal = min_len_transitions*integer
    total += subtotal
    print(line, subtotal, min_len_transitions, integer)
print(total)