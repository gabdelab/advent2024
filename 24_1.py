import re

initials = {}
gates = []

class Gate():
    def __init__(self, inA, inB, op, target):
        self.inA = inA
        self.inB = inB
        self.op = op
        self.target = target
        self.is_calculated = False

    def calculate(self):
        if self.inA not in initials or self.inB not in initials:
            return
        self.is_calculated = True
        if self.op == "AND":
            out = initials[self.inA] & initials[self.inB]
        elif self.op == "OR":
            out = initials[self.inA] | initials[self.inB]
        elif self.op == "XOR":
            out = initials[self.inA] ^ initials[self.inB]
        initials[self.target] = out

    def __repr__(self):
        return "%s %s %s -> %s" % (self.inA, self.op, self.inB, self.target)

with open("data/24.txt", "r") as file:
    wd = file.read()

sections = wd.split("\n\n")
for row in sections[0].split("\n"):
    initials[row.split(":")[0]] = int(row.split(":")[1])

for row in sections[1].split("\n"):
    target = row.split("->")[1].strip()
    right_side = row.split("->")[0].strip()
    print(right_side)
    inA = right_side.split(" ")[0]
    inB = right_side.split(" ")[2]
    op = right_side.split(" ")[1]
    gates.append(Gate(inA, inB, op, target))


print(initials)
print(gates)

while not all(i.is_calculated for i in gates):
    # print(len([i for i in gates if i.is_calculated]))
    for i in gates:
        i.calculate()

total = 0
for k in sorted(initials.keys(), reverse=True):
    if k.startswith("z"):
        total = 2 * total + initials[k]
print(total)