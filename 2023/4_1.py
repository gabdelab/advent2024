file = 'data/4.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    points = 0
    for row in data.split("\n"):
        row = row.split(":")[1]
        winning, mycards = row.split("|")

        winners = set([int(i.strip()) for i in winning.split(" ") if i.isdigit()])
        print(winners, mycards)
        cards = set([int(i.strip()) for i in mycards.split(" ") if i.isdigit()])
        intersect = len(cards.intersection(winners))

        if not intersect:
            continue
        points += 2**(intersect-1)
    print(points)