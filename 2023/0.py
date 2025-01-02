file = 'data/1.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    for row in data.split("\n"):
        print(row)