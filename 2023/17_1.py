import collections
import sys
file = 'data/17_ex.txt'
size = 13

sys.setrecursionlimit(15000)


datadict = {}
minima = {}
for i in range(size):
    minima[i] = {}
    for j in range(size):
        # minima[i][j] = {"n": {}, "w": {}, "s": {}, "e": {}}
        minima[i][j] = None

directions = ["n", "w", "s", "e"]

def next_row_col_from_direction(row, col, direction):
    orow, ocol = None, None
    if direction == "n":
        orow, ocol =  row-1, col
    if direction == "w":
        orow, ocol =  row, col-1
    if direction == "s":
        orow, ocol = row+1, col
    if direction == "e":
        orow, ocol = row, col+1
    return orow, ocol

def get_possible_paths():
    while


with open(file, 'r') as open_file:
    data = open_file.read()
for irow, row in enumerate(data.split("\n")):
    datadict[irow] = {}
    for icol, char in enumerate(row):
        datadict[irow][icol] = int(char)

