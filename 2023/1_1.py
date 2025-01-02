file = 'data/1txt'

digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
]

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    total = 0
    for row in data.split("\n"):
        if not row.strip():
            continue
        first_int = None
        last_int = None
        for i in row:
            if i.isdigit():
                if not first_int:
                    first_int = int(i)
                last_int = int(i)
        else:
            for index, digit in enumerate(digits):
                if row[0:len(digit)] == digit:
                    if not first_int:
                        first_int = index + 1
                    last_int = index + 1
        total += 10* first_int + last_int
    print(total)