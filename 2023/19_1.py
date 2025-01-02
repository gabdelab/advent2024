file = 'data/19.txt'

systems = {}

class Condition:

    def __init__(self, itype, quantity, side, destination):
        self.itype = itype
        self.quantity = quantity
        self.side = side # 1 for superior, 0 for inferior
        self.destination = destination

    def __repr__(self):
        return "%s %s %s %s" % (self.itype, self.quantity, self.side, self.destination)
    def route_input(self, input, cursor):
        if not self.itype:
            return self.destination, None
        if self.side == 1:
            if input[self.itype] > self.quantity:
                return self.destination, 0
            else:
                return None, cursor+1
        if self.side == 0:
            # print(input, self)
            if input[self.itype] < self.quantity:
                # print("returning here")
                return self.destination, 0
            else:
                return None, cursor+1

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    rules, datain = data.split("\n\n")
    for rule in rules.split("\n"):
        rulename, rule = rule[:-1].split("{")
        conditions = rule.split(",")
        for i in conditions:
            if i.find(":") == -1:
                mycond = Condition(None, None, None, i)
            else:
                condition, destination = i.split(":")
                if "<" in condition:
                    itype, quantity = condition.split("<")
                    mycond = Condition(itype, int(quantity), 0, destination)
                else:
                    itype, quantity = condition.split(">")
                    mycond = Condition(itype, int(quantity), 1, destination)
            try:
                systems[rulename].append(mycond)
            except KeyError:
                systems[rulename] = [mycond]

    total = 0
    for row in datain.split("\n"):
        irow = {}
        for input_data in row[1:-1].split(","):
            itype, quantity = input_data.split("=")
            irow[itype] = int(quantity)
        # print(irow)

        system = "in"
        cursor = 0
        while system not in ("A", "R"):
            # print("in", systems[system][cursor], system, cursor)
            out, cursor = systems[system][cursor].route_input(irow, cursor)
            # print("out", out, cursor)
            if cursor is None:
                # print("yolo", out)
                system = out
                cursor = 0
            if out:
                system = out

        if system == "A":
            print("found")
            total += sum(irow.values())
        if system == "R":
            print("unfound")

    print(total)