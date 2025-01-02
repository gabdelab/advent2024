file = 'data/13.txt'

def is_symetric(rows):
    if len(rows) == 1:
        return False
    if len(rows) < 2:
        return True
    return rows[0] == rows[-1] and is_symetric(rows[1:-1])


if __name__ == "__main__":
    with open(file, 'r') as open_file:
        data = open_file.read()
    total = 0
    for irow, puzzle in enumerate(data.split("\n\n")):
        if irow == 57:
            print(puzzle)
        found = False
        rows = puzzle.split("\n")
        # print("\nnew puzzle:\n", puzzle)
        nb_col = puzzle.find("\n")

        cols = ["" for _ in range(nb_col)]
        for j in rows:
            for index, char in enumerate(j):
                cols[index] = cols[index] + char
        nb_row = int((len(puzzle)+1) / (nb_col+1))
        # Remove left columns
        # Remove right columns
        # Remove top rows
        # Remove bottom rows
        for i in range(nb_row-1):
            if is_symetric(rows[i:]):
                found = True
                subtotal = int(100*(((nb_row+i) / 2)))
                total += subtotal
                print(irow, "found top rows", i+1, subtotal, total)
                break


        for i in range(1, nb_row-1):
            if is_symetric(rows[:-i]):
                found = True
                subtotal = int(100*(nb_row - i)/2)
                total += subtotal
                print(irow, "found bottom rows", i+1, subtotal, total)
                break



        for i in range(1, nb_col-1):
            if is_symetric(cols[:-i]):
                found = True
                subtotal =int((nb_col - i)/2) 
                total += subtotal
                print(irow, "found right cols", i+1, subtotal, total)
                break

        for i in range(nb_col-1):
            if is_symetric(cols[i:]):
                found = True
                subtotal = int( (((nb_col+i) / 2)))
                total += subtotal
                print(irow, "found left cols", i+1, subtotal, total)
                break

        if found:
            continue

        if not found:
            print("not found", cols)
    print(total)