from collections import OrderedDict
file = 'data/15.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    total = 0
    hashmap = {}
    for chars in data.split(","):
        chartype, label, position = None, None, None
        if chars.find("=") > -1:
            label, position = chars.split("=")
        elif chars.find("-") > -1:
            label = chars.split("-")[0]
        subtotal = 0
        for char in label:
            subtotal += ord(char)
            subtotal *= 17
            subtotal = subtotal % 256

        if hashmap.get(subtotal, None) is None:
            if position:
                hashmap[subtotal] = OrderedDict({label: int(position)})
        else:
            if hashmap[subtotal].get(label, None) is not None:
                if position:
                    hashmap[subtotal][label] = int(position)
                else:
                    hashmap[subtotal].pop(label)
            else:
                if position:
                    hashmap[subtotal][label] = int(position)
        print(hashmap)

    for k, v in hashmap.items():
        index = 0
        for k1, v1 in v.items():
            index += 1
            total += (int(k)+1) * index * v1

    print(total)


