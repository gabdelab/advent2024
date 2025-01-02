FILENAME = "data/21.txt"

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

def process_one_keyboard(line, is_numerical=True):
    # Given a line ex. 029A, return all possible lines to get there
    keyboard = NUMERICAL_KEYBOARD if is_numerical else DIGITAL_KEYBOARD
    reverse_keyboard = REVERSE_NUMERICAL_KEYBOARD if is_numerical else REVERSE_DIGITAL_KEYBOARD
    current_pos = reverse_keyboard["A"]
    out = []
    for char in line:
        char_pos = reverse_keyboard[char]
        if line == "456A" and char == "<" and current_pos == (0, 2):
            print("yoloswag2", path_vertical, path_horizontal)

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
        current_pos = reverse_keyboard[char]
    min_len = min(len(i) for i in out)
    return [i for i in out if len(i) == min_len]


def process(line):
    lines3 = []
    lines1 = process_one_keyboard(line, is_numerical=True)
    # print("line", line, "finished lines1, found", len(lines1), "lines", ''.join(lines1[0]))
    for i in lines1:
        lines2 = process_one_keyboard(i, is_numerical=False)
        #print("finished lines2, found", len(lines2), "lines", ''.join(lines2[0]))
        for j in lines2:
            line3 = process_one_keyboard(j, is_numerical=False)
            # print(line3)
            lines3.extend(line3)
    min_len = min(len(i) for i in lines3)
    for i in lines3:
        if len(i) == min_len:
            return i

data = []
with open(FILENAME, "r") as file:
    for line in file:
        data.append(line.strip())
print(data)

total = 0
for line in data:
    out = process(line)
    integer = int(line[:-1])
    subtotal = len(out)*integer
    total += subtotal
    print(subtotal, len(out), integer)
print(total)