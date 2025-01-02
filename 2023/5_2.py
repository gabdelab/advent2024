file = 'data/5.txt'

def split_interval(input, ranges):
    """
        Split a [x1: x2] interval with a [b1:b2] interval
    """

if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    seeds = []

    current_dest = []
    for session_index, section in enumerate(data.split("\n\n")):
        print("yolo %d" % (session_index))
        if session_index == 0:
            seeds = [int(i) for i in section.split(":")[1].split(" ") if i.isdigit()]
            for i in range(0, len(seeds), 2):
                current_dest.append((seeds[i], seeds[i]+seeds[i+1]))
            continue
        ranges = []

        print("in_basket: %s" % (current_dest))

        for irow, row in enumerate(section.split("\n")):
            if irow == 0:
                continue
            out_range_start, in_range_start, range_len = [int(i) for i in row.split(" ") if i.isdigit()]
            ranges.append((in_range_start, in_range_start+range_len-1, out_range_start - in_range_start))
        
        next_dest = []
        in_basket = current_dest

        print("ranges: %s" % (ranges))
        while in_basket:
            print("current in_basket: %s; current_dest: %s" % (in_basket, next_dest))
            i = in_basket.pop()
            found = False 
            in_start = i[0]
            in_end = i[1]

            # For each interval, check if it intersects our range. 3 scenarios:
            # - it contains fully our range: if so we add delta and we break
            # - it contains partially our range: if so we add delta to the partial match, exclude the partial match and continue
            # - it contains none of our range: if so we continue
            # At the end we keep the remaining parts
            for j in ranges:
                r_start = j[0]
                r_end = j[1]
                delta = j[2]

                # Case 1: our seed is fully into the range
                if r_start <= in_start and r_end >= in_end:
                    found = True
                    print("seed: %s - range %s - fully into range" % (i, j))
                    next_dest.append((in_start+delta, in_end+delta))
                    break

                # Case 2: our seed is completely out of the range
                if r_start > in_end or r_end < in_start:
                    # print("seed: %s - range %s - fully out of range" % (i, j))
                    # next_dest.append((in_start, in_end))
                    continue

                # Case 3: the range is fully into the seed
                if r_start >in_start and r_end < in_end:
                    found = True
                    print("seed: %s - range %s - range fully into seed" % (i, j))
                    next_dest.append((r_start+delta, r_end+delta))
                    in_basket.append((in_start, r_start-1))
                    in_basket.append((r_end+1, in_end))
                    break

                # Case 4: the range starts before the end of the seed
                if r_start <=in_start:
                    found = True
                    print("seed: %s - range %s - range starts before seed" % (i, j))
                    next_dest.append((in_start+delta, r_end+delta))
                    in_basket.append((r_end+1, in_end))
                    break

                # Case 5: the range ends after the start of the seed
                if r_end >= in_end:
                    found = True
                    print("seed: %s - range %s - seed starts before range" % (i, j))
                    next_dest.append((r_start+delta, in_end+delta))
                    in_basket.append((in_start, r_start-1))
                    break
            if not found:
                print("never found")
                next_dest.append((in_start, in_end))
        current_dest = next_dest

        # print(ranges)
        print(current_dest)
    print(min([i[0] for i in current_dest]))


    #     out_dest = []
    #     print("yolo")
    #     for i in current_dest:
    #         found = False
    #         for irange in ranges:
    #             if found or i < irange[0] or i >= irange[1]:
    #                 break
    #             if i >= irange[0] and i < irange[1]:
    #                 out_dest.append(i+irange[2])
    #                 found = True
    #         if not found:
    #             out_dest.append(i)
    #     current_dest = out_dest
    # print(min(current_dest))