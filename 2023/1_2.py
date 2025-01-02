file = 'data/1.txt'

digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
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
        for i0, i in enumerate(row):
            if i.isdigit():
                if not first_int:
                    first_int = int(i)
                last_int = int(i)
            else:
                for index, digit in enumerate(digits):
                    if row[i0:i0+len(digit)] == digit:
                        if not first_int:
                            first_int = index + 1
                        last_int = index + 1
        print(first_int, last_int)
        total += 10* first_int + last_int
    print(total)