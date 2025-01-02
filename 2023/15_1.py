file = 'data/15.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    total = 0
    for chars in data.split(","):
        subtotal = 0
        for char in chars:
            subtotal += ord(char)
            subtotal *= 17
            subtotal = subtotal % 256
        total += subtotal
    print(total)
