from itertools import combinations

file = 'data/12.txt'

def evaluate(word, expectations):
    """Return true if a word matches expectations

    where word is a "....####.#.#.#.##.#.#."
    and expectations is (1,1,3,2,3)
    """
    print(word, expectations)
    if word == "" and not expectations:
        return True
    if word == "" and expectations:
        return False
    if word[0] == ".":
        return evaluate(word[1:], expectations)
    if not expectations:
        return False
    # If we're here it means word[0] is a #
    if expectations[0] == 1:
        # print(word, expectations)
        return (word == "#" or word[1] == ".") and evaluate(word[1:], expectations[1:])

    if word[1] == ".":
        return False
    exp = expectations.copy()
    exp[0] -= 1
    return evaluate(word[1:], exp)


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()

    total = 0
    for row in data.split("\n"):
        print(row)
        local_total = 0

        chars, data = row.split(" ")

        total_unknown = 0
        total_filled = 0
        unknown_positions = []
        for index, char in enumerate(chars):
            if char == "?":
                total_unknown += 1
                unknown_positions.append(index)
            if char == "#":
                total_filled += 1

        expectations = [int(i) for i in data.split(",")]

        total_expectations = sum(expectations)


        to_fill = total_expectations - total_filled

        for i in combinations(range(total_unknown), to_fill):
            mycopy = chars
            for index, j in enumerate(unknown_positions):
                if index in i:
                    mycopy = mycopy[:j] + "#" + mycopy[j+1:]
                else:
                    mycopy = mycopy[:j] + "." + mycopy[j+1:]
            # print("yolo", mycopy, i, unknown_positions)
            if evaluate(mycopy, expectations.copy()):
                print(mycopy, expectations, "combination", i, "unknown_positions", unknown_positions)
                # print("found", mycopy, i, expectations)
                local_total += 1

        print(local_total)
        total += local_total

    print(total)