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
            if input[self.itype] < self.quantity:
                return self.destination, 0
            else:
                return None, cursor+1

class Interval:

    def __init__(self, astart, aend, mstart, mend, xstart, xend, sstart, send, system, cursor):
        self.a_start = astart
        self.a_end = aend
        self.m_start = mstart
        self.m_end = mend
        self.x_start = xstart
        self.x_end = xend
        self.s_start = sstart
        self.s_end = send
        self.system = system
        self.cursor = cursor

    def size(self):
        if self.system != "A":
            return 0
        return (self.a_end-self.a_start+1)*(self.m_end-self.m_start+1) \
            *(self.s_end-self.s_start+1)*(self.x_end-self.x_start+1)

    def set(self, value, itype, boundaries):
        if itype == "a":
            if boundaries == "s":
                self.a_start = value
            else:
                self.a_end = value
        if itype == "s":
            if boundaries == "s":
                self.s_start = value
            else:
                self.s_end = value
        if itype == "x":
            if boundaries == "s":
                self.x_start = value
            else:
                self.x_end = value
        if itype == "m":
            if boundaries == "s":
                self.m_start = value
            else:
                self.m_end = value


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

    # An interval of [1-4000] on a, s, x and m enters "in"
    # Two intervals exit the first condition:
    # - An interval of [1-1351]s X [1-4000]a X [1-4000]x X [1-4000]m enters "px" with cursor 0
    # - An interval of [1352-4000]s X [1-4000]a X [1-4000]x X [1-4000]m continues in "in" with cursor 1
    intervals = [Interval(1, 4000, 1, 4000, 1, 4000, 1, 4000, "in", 0)]
    sorted_intervals = []
    discarded_intervals = []
    while intervals:
        i = intervals[0]
        if i.system == "A":
            sorted_intervals.append(i)
            intervals.pop(0)
            continue
        if i.system == "R":
            discarded_intervals.append(i)
            intervals.pop(0)
            continue
        system = systems[i.system][i.cursor]
        if not system.itype:
            i.system = system.destination
            i.cursor = 0
            continue
        quantity = system.quantity
        side = system.side
        itype = system.itype 

        i2 = Interval(i.a_start, i.a_end, i.m_start, i.m_end, i.x_start, i.x_end, i.s_start, i.s_end, i.system, i.cursor)
        if side == 0:
            i.set(quantity - 1, itype, "e")
            i.cursor = 0
            i.system = system.destination
            i2.set(quantity, itype, "s")
            i2.cursor = i2.cursor + 1
        if side == 1:
            i.set(quantity + 1, itype, "s")
            i.cursor = 0
            i.system = system.destination
            i2.set(quantity, itype, "e")
            i2.cursor = i2.cursor + 1
        intervals.append(i2)
        print(sorted_intervals)
    print(sum([i.size() for i in sorted_intervals]))

    # intervals = {"s": {4000: "in"}, "x": {4000: "in"}, "m": {4000: "in"}, "a": {4000: "in"}}

    # system = "in"
    # cursor = 0
    # while True:
    #     all_keys = [i.values() for i in intervals.values()]
    #     if set(all_keys) == {"A", "R"}:
    #         break
    #     condition = systems[system][cursor]
    #     if condition == 1:
    #     # Split up conditions

    #     # Add the new condition
    #     intervals[condition.itype]
    # print(intervals)


    # total = 0
    # for a in range(4000):
    #     print(a)
    #     for m in range(4000):
    #         for x in range(4000):
    #             for s in range(4000):
    #                 irow = {"a": a+1, "s": s+1, "m": m+1, "x": x+1}
    #                 system = "in"
    #                 cursor = 0
    #                 while system not in ("A", "R"):
    #                     # print("in", systems[system][cursor], system, cursor)
    #                     out, cursor = systems[system][cursor].route_input(irow, cursor)
    #                     # print("out", out, cursor)
    #                     if cursor is None:
    #                         # print("yolo", out)
    #                         system = out
    #                         cursor = 0
    #                     if out:
    #                         system = out

    #                 if system == "A":
    #                     total += 1

    # print(total)