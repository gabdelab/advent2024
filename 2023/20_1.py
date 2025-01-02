file = 'data/20.txt'

class Module:

    def __init__(self, mtype, mname, directions):
        self.name = mname
        self.type = mtype
        self.directions = directions
        self.state = "off" if self.type == "ff" else None
        self.connected = {} if self.type == "c" else None
        self.found_index = None

    def __repr__(self):
        return "%s - %s - %s (%s)" % (self.name, self.type, self.state, self.connected)

    def set_connected(self, connected):
        if self.connected is None:
            return
        self.connected[connected] = "low"

    def get_next_signals(self, signal, input):
        if self.name == "broadcaster":
            return [(i, "low", self.name) for i in self.directions]
        if self.type == "ff":
            if signal == "high":
                return []
            if self.state == "on":
                self.state = "off"
                return [(i, "low", self.name) for i in self.directions]
            else:
                self.state = "on"
                return [(i, "high", self.name) for i in self.directions]
        if self.type == "c":
            # Update the in-memory for that input
            self.connected[input] = signal
            if all(i == "high" for i in self.connected.values()):
                return [(i, "low", self.name) for i in self.directions]
            else:
                return [(i, "high", self.name) for i in self.directions]
        if self.type == None:
            return []
if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()

    modules = {}
    for row in data.split("\n"):
        module, directions = row.split(" -> ")
        directions = directions.split(", ")
        mname = module
        mtype = None
        if module[0] == "%":
            mtype = "ff"
            mname = module[1:]
        if module[0] == "&":
            mtype = "c"
            mname = module[1:]

        modules[mname] = Module(mtype, mname, directions)
        if "output" in directions:
            modules["output"] = Module(None, "output", [])
        if "rx" in directions:
            modules["rx"] = Module(None, "rx", [])

    for key, module in modules.items():
        for direction in module.directions:
            modules[direction].set_connected(key)

    print(modules["df"])
    items = [("broadcaster", "low", None)]
    button = 1
    index = 0
    while True:
        empty = False
        index += 1
        if button % 100000 == 0 and index % 1000000 == 0:
            print(button)
        if items == []:
            empty = True
            connected = modules["df"].connected
            if any([i == "high" for i in connected.values()]):
                print(connected, button)
            # print([modules[m].state for m in modules["df"].connected])
            button += 1
            items = [("broadcaster", "low", None)]
        first_item = items.pop(0)
        module = modules[first_item[0]]
        signal = first_item[1]
        last_signal = first_item[2]
        if signal == "low" and module == "rx":
            break
        next_signals = module.get_next_signals(signal, last_signal)
        if module.type == "c" and next_signals and next_signals[0][1] == "low" and not module.found_index:
            module.found_index = button
            print("found index", button, module.name, [m for m in modules.values() if m.type == "c"])
        items.extend(next_signals)

    print(button)
    print(modules)