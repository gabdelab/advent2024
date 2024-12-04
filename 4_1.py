data = []
rows = []

def count_subrows_in_row(row, subrow):
    counter = 0
    for i in range(len(row)):
        if row[i:i+len(subrow)] == subrow:
            counter += 1
    return counter

with open("data/4.txt", "r") as file:
    lines = file.readlines()

nb_rows = len(lines)
print(nb_rows)
upwards_diagonals = {i: [] for i in range(2*nb_rows)}
downwards_diagonals = {i: [] for i in range(2*nb_rows)}
cols = {i: [] for i in range(nb_rows)}
for linenumber, line in enumerate(lines):
    line = line.strip()
    rows.append(list(line))
    for colnumber, col in enumerate(list(line)):
        cols[colnumber].append(col)
        downwards_diagonals[nb_rows+colnumber-linenumber-1].append(col)
        upwards_diagonals[colnumber+linenumber].append(col)

print(downwards_diagonals, upwards_diagonals, rows, cols)

prev_counter = 0
counter = 0
for row in rows:
    counter += count_subrows_in_row(row, list("XMAS"))
print("rows XMAS", counter - prev_counter)
prev_counter = counter
for row in rows:
    counter += count_subrows_in_row(row, list("SAMX"))
print("rows SAMX", counter - prev_counter)
prev_counter = counter
for col in cols.values():
    counter += count_subrows_in_row(col, list("XMAS"))
print("cols XMAS", counter - prev_counter)
prev_counter = counter
for col in cols.values():
    counter += count_subrows_in_row(col, list("SAMX"))
print("cols SAMX", counter - prev_counter)
prev_counter = counter
for downwards_diagonal in downwards_diagonals.values():
    counter += count_subrows_in_row(downwards_diagonal, list("XMAS"))
print("downwards_diagonals XMAS", counter - prev_counter)
prev_counter = counter
for downwards_diagonal in downwards_diagonals.values():
    counter += count_subrows_in_row(downwards_diagonal, list("SAMX"))
print("downwards_diagonals SAMX", counter - prev_counter)
prev_counter = counter
for upwards_diagonal in upwards_diagonals.values():
    counter += count_subrows_in_row(upwards_diagonal, list("XMAS"))
print("upwards_diagonals XMAS", counter - prev_counter)
prev_counter = counter
for upwards_diagonal in upwards_diagonals.values():
    counter += count_subrows_in_row(upwards_diagonal, list("SAMX"))
print("upwards_diagonals SAMX", counter - prev_counter)

print("total", counter)