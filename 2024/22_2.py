test = False

if test:
    FILENAME = "data/22_ex_2.txt"
else:
    FILENAME = "data/22.txt"

combinations = {}

def compute_next(secret):
    initial_secret = secret
    # Step 1
    new_secret = secret * 64
    secret = new_secret ^ secret
    secret = secret % 16777216
    # Step 2
    new_secret = int(secret / 32)
    secret = new_secret ^ secret
    secret = secret % 16777216
    # Step 3
    new_secret = secret * 2048
    secret = new_secret ^ secret
    secret = secret % 16777216
    return secret


data = []
with open(FILENAME, "r") as file:
    for line in file:
        data.append(int(line.strip()))

max_gain = 0
for initial_row in data:
    row = initial_row
    rows = [row%10]
    for iteration in range(2000):
        row = compute_next(row)
        rows.append(row%10)
    diffs = [rows[i+1] - rows[i] for i in range(len(rows)-1)]

    for i, j in enumerate(diffs[:-3]):
        suite = "/".join(map(str, diffs[i:i+4]))

        if suite not in combinations.keys():
            combinations[suite] = {initial_row: rows[i+4]}
        elif suite in combinations.keys() and initial_row not in combinations[suite].keys():
            combinations[suite][initial_row] = rows[i+4]
        elif suite in combinations.keys() and initial_row in combinations[suite].keys():
            continue
        else:
            raise ValueError("Something went wrong")

for entry, values in combinations.items():
    if sum(values.values()) > max_gain:
        print(entry, sum(values.values()))
    max_gain = max(max_gain, sum(values.values()))


print(max_gain)