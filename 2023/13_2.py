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


    for irow, opuzzle in enumerate(data.split("\n\n")):
        found = False
        rows = opuzzle.split("\n")
        # print("\nnew opuzzle:\n", opuzzle)
        nb_col = opuzzle.find("\n")

        cols = ["" for _ in range(nb_col)]
        for j in rows:
            for index, char in enumerate(j):
                cols[index] = cols[index] + char
        nb_row = int((len(opuzzle)+1) / (nb_col+1))
        # Remove left columns
        # Remove right columns
        # Remove top rows
        # Remove bottom rows
        for i in range(nb_row-1):
            if is_symetric(rows[i:]):
                sfound = "t"+str(i)
                break
        for i in range(1, nb_row-1):
            if is_symetric(rows[:-i]):
                sfound = "b"+str(i)
                break
        for i in range(1, nb_col-1):
            if is_symetric(cols[:-i]):
                sfound = "l"+str(i)
                break

        for i in range(nb_col-1):
            if is_symetric(cols[i:]):
                sfound = "r"+str(i)
                break

        print("@@@@@@", sfound)
        exitfound = False
        for ipuzzle, char in enumerate(opuzzle):
            if exitfound:
                continue
            puzzle = opuzzle
            if puzzle[ipuzzle] == "\n":
                continue
            repl = "." if puzzle[ipuzzle] == "#" else "."
            puzzle = puzzle[:max(ipuzzle, 0)] + repl + puzzle[ipuzzle+1:]
            if ipuzzle == 0:
                print(puzzle)
            rows = puzzle.split("\n")
            # print("\nnew puzzle:\n", puzzle)
            nb_col = puzzle.find("\n")

            cols = ["" for _ in range(nb_col)]
            for j in rows:
                for index, char in enumerate(j):
                    cols[index] = cols[index] + char
            nb_row = int((len(puzzle)+1) / (nb_col+1))

            nbfound = 0
            # Remove left columns
            # Remove right columns
            # Remove top rows
            # Remove bottom rows
            for i in range(nb_row-1):
                if is_symetric(rows[i:]):
                    if "t" + str(i) == sfound:
                        continue

                    ofound = "t"+str(i)
                    found = True
                    subtotal = int(100*(((nb_row+i) / 2)))
                    # print(irow, "found top rows", i+1, subtotal, total)
                    nbfound += 1
                    break


            for i in range(1, nb_row-1):
                if is_symetric(rows[:-i]):
                    if "b" + str(i) == sfound:
                        continue

                    ofound = "b"+str(i)
                    print("michel galabru", ofound)
                    found = True
                    subtotal = int(100*(nb_row - i)/2)
                    # print(irow, "found bottom rows", i+1, subtotal, total)
                    nbfound += 1
                    break



            for i in range(1, nb_col-1):
                if is_symetric(cols[:-i]):
                    if "l" + str(i) == sfound:
                        continue

                    ofound = "l"+str(i)
                    found = True
                    subtotal =int((nb_col - i)/2) 
                    # print(irow, "found right cols", i+1, subtotal, total)
                    nbfound += 1
                    break

            for i in range(nb_col-1):
                if is_symetric(cols[i:]):
                    if "r" + str(i) == sfound:
                        continue
                    ofound = "r"+str(i) 
                    found = True
                    subtotal = int( (((nb_col+i) / 2)))
                    # print(irow, "found left cols", i+1, subtotal, total)
                    nbfound += 1
                    break

            if found:
                print("yoloswag", ipuzzle, opuzzle, "vs", puzzle)
                total += subtotal
                exitfound = True
                continue


            if nbfound > 1:
                print("yolo")

            if not found:
                print("not found", cols)
    print(total)