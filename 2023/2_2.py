import re


file = 'data/2.txt'


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    total = 0
    for index, game in enumerate(data.split("\n")):
        game = game.split(":")[1]
        maxima = {}
        for condition in game.split(";"):
            for color_condition in condition.split(","):
                quantity, colorcode = color_condition.split()
                if maxima.get(colorcode, None) is not None:
                    maxima[colorcode] = max(int(quantity), maxima[colorcode])
                else:
                    maxima[colorcode] = int(quantity)
        power = 1
        for k, v in maxima.items():
            power *= v
        total += power
        print(index, maxima, power)
    print(total)