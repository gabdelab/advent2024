test = False

if test:
    FILENAME = "data/22_ex.txt"
else:
    FILENAME = "data/22.txt"

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

total = 0
for row in data:
    initial_row = row
    for iteration in range(2000):
        row = compute_next(row)
    total += row
    print("row", initial_row, "contributed", row)

print(total)