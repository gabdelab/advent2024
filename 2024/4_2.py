data = []
rows = []

with open("data/4.txt", "r") as file:
    lines = file.readlines()

for linenumber, line in enumerate(lines):
    rows.append(list(line.strip()))


counter = 0

for irow, row in enumerate(rows):
    if irow == 0 or irow == len(rows)-1:
        continue
    for icol, col in enumerate(row):
        if icol == 0 or icol == len(rows)-1:
            continue
        print(irow, icol)
        if col == "A":
            if ((rows[irow-1][icol+1] == "M" and rows[irow+1][icol-1] == "S") and (rows[irow-1][icol-1] == "M" and rows[irow+1][icol+1] == "S")) or \
                ((rows[irow-1][icol+1] == "M" and rows[irow+1][icol-1] == "S") and (rows[irow-1][icol-1] == "S" and rows[irow+1][icol+1] == "M")) or \
                ((rows[irow-1][icol+1] == "S" and rows[irow+1][icol-1] == "M") and (rows[irow-1][icol-1] == "M" and rows[irow+1][icol+1] == "S")) or \
                ((rows[irow-1][icol+1] == "S" and rows[irow+1][icol-1] == "M") and (rows[irow-1][icol-1] == "S" and rows[irow+1][icol+1] == "M")):
                print("found")
                counter += 1
print(counter)