file = 'data/4.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    points = 0
    copies = {i: 1 for i in range(len(data.split("\n")))}

    print(copies)
    for index, row in enumerate(data.split("\n")):
        row = row.split(":")[1]
        winning, mycards = row.split("|")

        winners = set([int(i.strip()) for i in winning.split(" ") if i.isdigit()])
        cards = set([int(i.strip()) for i in mycards.split(" ") if i.isdigit()])
        intersect = len(cards.intersection(winners))

        if not intersect:
            continue
        
        copier = copies[index]
        while intersect:
            copies[index+intersect] += copier
            intersect -= 1

    print(copies)
    print(sum(copies.values()))