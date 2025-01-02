file = 'data/5.txt'

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    seeds = []

    for session_index, section in enumerate(data.split("\n\n")):
        if session_index == 0:
            seeds = [int(i) for i in section.split(":")[1].split(" ") if i.isdigit()]
            current_dest = seeds
            print(current_dest)
            continue
        ranges = []
        for irow, row in enumerate(section.split("\n")):
            if irow == 0:
                continue
            out_range_start, in_range_start, range_len = [int(i) for i in row.split(" ") if i.isdigit()]
            ranges.append([in_range_start, in_range_start+range_len, out_range_start - in_range_start])
        out_dest = []
        for i in current_dest:
            found = False
            for irange in ranges:
                if i >= irange[0] and i < irange[1]:
                    if found:
                        raise ValueError("impossible to get there")
                    out_dest.append(i+irange[2])
                    found = True
            if not found:
                out_dest.append(i)
        current_dest = out_dest
        print(current_dest)
    print(current_dest)
    print(min(current_dest))